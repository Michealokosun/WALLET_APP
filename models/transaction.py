#!/usr/bin/env python
import datetime
from typing import optional

class transaction:
    def __init__(self) -> None:
            pass
    
    def transaction_id(self,transaction_id):
        """ unique identifier for each transaction"""
          self.transaction_id = transaction_id
          return self.transaction_id
    
    def timestamp(self,timestamp):
        """date and  time when the transaction occured"""
          self.timestamp = timestamp
          return self.timestamp

    def sender(self,sender):
        """wallet account that sent the funds"""
          self.sender = sender
          return self.sender

    def receiver(self,receiver):
        """wallet account that received the funds"""
          self.receiver = receiver
          return self.receiver

    def amount(self,amount):
        """quantity of currency transfered in the  transaction"""
          self.amount = amount
          return self.amount

    def status(self,status):
        """the current status of the transaction like pending,completed or failed"""
          self.status = status
          return self.status
    
    def get_formatted_amount(self):
          return f"{self.amount:.2f}"
