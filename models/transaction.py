#!/usr/bin/env python
import datetime
ffrom typing import optional

class transaction:
    def __init__(self) -> None:
            pass
    
    def transaction_id(self,transaction_id):
          self.transaction_id = transaction_id
          return self.transaction_id
    
    def timestamp(self,timestamp):
          self.timestamp = timestamp
          return self.timestamp
    def sender(self,sender):
          self.sender = sender
          return self.sender
    def receiver(self,receiver):
          self.receiver = receiver
          return self.receiver
    def amount(self,amount):
          self.amount = amount
          return self.amount
    def status(self,status):
          self.status = status
          return self.status
    
    def get_formatted_amount(self):
          return f"{self.amount:.2f}"
