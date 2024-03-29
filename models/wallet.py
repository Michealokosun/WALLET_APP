#!/usr/bin/env python

from uuid import uuid4
import bcrypt
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from  sqlalchemy.orm import relationship
from models.basemodel import Base, BaseModel
from models.transaction import Transaction
from models.transaction import Transaction


class Wallet(BaseModel, Base):
    __tablename__ = 'wallets'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    balance = Column(Integer, default=0)
    wallet_type = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'balance' in kwargs:
            self.balance = kwargs['balance']
        else:
            self.balance = 0

    def deposit(self, amount):
        transaction = Transaction(type='deposit', wallet_id = self.id, initial_balance = self.balance)
        self.balance += amount
        transaction.final_balance = self.balance
        transaction.save()
        return self.balance

    def withdraw(self, amount):
        assert self.balance >= amount > 0, "Insufficient balance for withdrawal"
        transaction = Transaction(type='withdrawal', wallet_id = self.id, initial_balance = self.balance)
        self.balance -= amount
        transaction.final_balance = self.balance
        transaction.save()
        return self.balance

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, reciepient_wallet_id):
        from models import storage
    
        assert self.balance >= amount > 0, "Insufficient balance for transfer"
        transaction = Transaction(type='transfer', wallet_id = self.id, initial_balance = self.balance)
        reciepient_wallet = storage.get(Wallet, id=reciepient_wallet_id)
        if reciepient_wallet:
            self.balance -= amount
            reciepient_wallet.balance += amount
            transaction.final_balance = self.balance
            transaction.save()
            reciepient_wallet_transaction = Transaction(type='deposit', wallet_id = reciepient_wallet.id,
                                                        initial_balance = reciepient_wallet.balance - amount, final_balance = reciepient_wallet.balance)
        reciepient_wallet_transaction.save()
        return self.balance, reciepient_wallet.balance
    