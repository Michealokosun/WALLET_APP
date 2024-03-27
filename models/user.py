#!/usr/bin/env pyhton

import bcrypt
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from  sqlalchemy.orm import relationship
from models.basemodel import Base, BaseModel
from models.wallet import Wallet

class User(BaseModel, Base):
    """
    User account model
    """
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    surname = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=True)
    email = Column(String(255), nullable=False, unique=True)
    address = Column(String(255), nullable=True)
    password = Column(LargeBinary, nullable=False)
    wallet_id = Column(String(255), ForeignKey("users.id"), nullable=True)

    wallet = relationship("Wallet", backref="user", cascade="all, delete, delete-orphan")


    def __init__(self, **data):
        super().__init__(**data)
        if 'password' in data:
            self.password = self.hash_password(data['password'])
        if 'wallet_type' in data:
            self.wallet = [Wallet(user_id=self.id, wallet_type=data['wallet_type'])]
        else:
            self.wallet = [Wallet(user_id=self.id, wallet_type='savings')]

    def hash_password(self, password):
        """Hash the password before saving it"""
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    
    def check_password(self, password):
        """Check the password during login"""
        return bcrypt.checkpw(password.encode('utf8'), self.password)