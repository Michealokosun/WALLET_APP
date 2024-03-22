import uuid0

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    user_name:str
    personal_website : str = None
    phone_number : int
    email_address: str
    employee_id: str
    employee_uuid: str = None
    

#TODO add encryption for sensitive data
def generate_uuid(input_data:dict) -> str:
    user_details = input_data
    uuid = str(uuid0.generate())
    return uuid


