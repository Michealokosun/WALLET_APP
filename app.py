#!/usr/bin/env python
"""Contains the flask app"""


from models import storage
from flask import request, jsonify, abort
from models.user import User
from models.transaction import Transaction
from models.wallet import Wallet

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route("/users")
def get_users():
    """
    Get all User objects from storage and return them in a JSON response.
    If no users exist, return a 404 error.
    """
    users = storage.get_all(User)
    if users:
        return jsonify({user.to_dict() for user in users})
    abort(404)



@app.route("/sign_up")
def sign_up():
    # Create a user account and wallet account from the user class
    """
    Creates a new user account if the email does not already exist.
    Gets the user data from the request JSON. Checks if a user already 
    exists with that email. If not, creates a new User object from the 
    request data and saves it to storage. Returns appropriate success or
    error messages.
    request params: if nullable, it is not required.
    surname =  nullable=False
    firstname =  nullable=False
    lastname =  nullable=True
    email =  nullable=False, unique=True
    address =  nullable=True
    password = nullable=False
    """
   
    data = request.get_json()
    user = storage.get(User, email=data['email'])
    if user:
        return "User already exists"
    else:
        user= User(**request.get_json())
        user.save()
        return "User account created "


@app.route("/sign_in")
def sign_in():
     # signs into a user account and corresponding wallet account(s) for the user
    """
    signs in an existing user.
    request params: if nullable, it is not required.
    surname =  nullable=False
    firstname =  nullable=False
    lastname =  nullable=True
    email =  nullable=False, unique=True
    address =  nullable=True
    password = nullable=False
    """
    data = request.get_json()
    user_email = storage.get(User, email=data["email"])
    user_password = storage.get(User, email=data["password"])
    # if user:
    #     return "User already exists"
    # else:
    #     user= User(**request.get_json())
    #     user.save()
    #     return "User account created "
    
    # signs the user in 
    return "Welcome"

@app.route("/create_wallet")
def create_wallet():
    """
    Creates a new Wallet object from the request JSON data
    and saves it to the storage.
    user_id: nullable=false
    balance: nullable=true
    wallet_type: nullable=false
    """
    wallet = Wallet(**request.get_json())
    wallet.save()    

@app.route('/deposit')
def deposit_funds(amount,user_id):
    data = request.get_json()
    amount = data["amount"]
    if amount <= 0:
        return "invalid amount"
    try:
        wallet = storage.get(Wallet, id=data["id"])
        if not wallet:
            return "Wallet not found"
        else:
            wallet.deposit(amount)
            return "Deposit successful"
    except Exception as e:
        print(e)
    
    #locate user wallet and add funds should return a successful or failed message and current balance

@app.route('/withdraw')
def withdraw_funds(amount,user_id):
    data = request.get_json()
    amount = data["amount"]
    if amount <= 0:
        return "invalid amount"
    try:
        wallet = storage.get(Wallet, id=data["id"])
        if not wallet:
            return "Wallet not found"
        else:
            balance = wallet.withdraw(amount)
            return f"withdraw successful balance is {balance}"
    except Exception as e:
        print(e)
    
    
    #locate user wallet and subtract funds should return a successful or failed message and current balance

@app.route('/transfer')
def transfer_funds():
    """
    
    
    """
    #TODO add request param documentation
    data = request.get_json()
    amount = data["amount"]
    receiver_wallet_id = data["wallet_id"]
    if amount <= 0:
        return "invalid amount"
    try:
        sender_wallet = storage.get(Wallet, id=data["sender_id"])
        if not wallet:
            return "Wallet not found"
        else:
            balance = wallet.transfer(amount, receiver_wallet_id)
            return f"Transfer successful your balance is {balance}"
    except Exception as e:
        print(e)
    #locate user wallet and subtract funds should return a successful or failed message and current balance
@app.route('/get_balance')

def get_balance(user_id):
    data = request.get_json()
    try:
        wallet = storage.get(Wallet, id=data["id"])
        if not wallet:
            return "Wallet not found"
        else:
            balance = wallet.get_balance()
            return f"Your balance is {balance}"
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=True)