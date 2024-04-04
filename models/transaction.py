#!/usr/bin/env python

"""the transaction module"""

from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey

class Transaction(BaseModel, Base):
    """the transaction class"""
    __tablename__ = 'transactions'

    id = Column(String, primary_key=True)
    type = Column(String(256), nullable=False)
    wallet_id = Column(String, ForeignKey('wallets.id'))
    initial_balance = Column(Integer, nullable=False)
    final_balance = Column(Integer)