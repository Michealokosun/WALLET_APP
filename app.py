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
    users = storage.get_all(User)
    if users:
        return jsonify({user.to_dict() for user in users})
    abort(404)



@app.route("/sign_in")
def sign_in():
    # signs the user in 
    return "sign in"

@app.route("/create_account")
def create_wallet_account(user_info):
    user_info = request.get_json()
    # encode with JWT, should return an id

@app.route('/deposit')
def deposit_funds(amount,user_id):
    amount = request.get_json()['amount']
    #locate user wallet and add funds should return a successful or failed message and current balance

@app.route('/withdraw')
def withdraw_funds(amount,user_id):
    amount = request.get_json()['amount']
    #locate user wallet and subtract funds should return a successful or failed message and current balance

@app.route('/transfer')
def transfer_funds(amount,user_id,receiving_wallet_id):
    amount = request.get_json()['amount']
    #locate user wallet and subtract funds should return a successful or failed message and current balance
@app.route('/get_balance')
def get_balance(user_id):
    #verify user existence and return balance
    return "balance"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=True)