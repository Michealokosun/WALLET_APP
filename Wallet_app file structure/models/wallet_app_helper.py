# import uuid0
import jwt
from pydantic import BaseModel, ValidationError


class User(BaseModel):
#Make it so that the user name or email can be used to sign into the account
    user_name:str
    phone_number : int 
    email_address: str
    # encode: str 
    employee_uuid: str = None
    
KEY = "secret"


#TODO add encryption for sensitive data
def generate_uuid(input_data:dict) -> str:
    # will serve as unique customer identifier
    user_details = input_data
    uuid = str(uuid0.generate())
    return uuid


def sign_in(user_information):
    """
        Tries to validate the user information against the User model.
        If validation fails, prints the errors.
        Then encodes the user information into a JWT token using the secret key.
        Returns the encoded token.
   """
    try:
        data = User(user_information)
    except ValidationError as e:
        print(e.errors())
    encoded = jwt.encode(user_information, KEY, algorithm="HS256")
    return encoded
    
    
def generate_wallet_account(user_information):
    """Generates an encoded jwt token from user information then uses that verify access to create and access a table in the db"""
    # creates a uuid for the user that will be used
    user_information["uuid"] = generate_uuid(user_information)



