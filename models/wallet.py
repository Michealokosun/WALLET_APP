#!/usr/bin/env python

from uuid import uuid4
import bcrypt
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from  sqlalchemy.orm import relationship
from models.basemodel import Base, BaseModel

class Wallet(BaseModel, Base):
    __tablename__ = 'wallets'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    balance = Column(Integer, default=0)
    wallet_type = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        assert self.balance >= amount > 0, "Insufficient balance for withdrawal"
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance