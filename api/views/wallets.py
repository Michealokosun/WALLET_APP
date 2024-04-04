#!/usr/bin/env python
"""the wallet view"""

from flask import jsonify, request, abort
from api.views import app_views
from models import storage
from models.wallet import Wallet
from models.user import User
from models.transaction import Transaction
from psycopg2 import errors
from sqlalchemy.exc import SQLAlchemyError
from api.views.utils.token_required import token_required


@app_views.route('/wallets', methods=['GET'], strict_slashes=False)
@token_required
def get_all_wallets():
    """
    query-> SELECT * FROM wallets 
    [Returns a dictionary (key:obj) object for easy indexing]
    """
    wallets = storage.get_all(Wallet)
    if not wallets:
        abort(404)
    return jsonify([wallet.to_dict() for wallet in wallets])

@app_views.route('/wallets/<wallet_id>', methods=['GET'], strict_slashes=False)
@token_required
def get_wallet_by_id(wallet_id):
    """
    query-> SELECT * FROM wallet where id=wallet_id
    Returns a wallet object
    """
    
    wallet = storage.get(Wallet, id=wallet_id)
    if not wallet:
        abort(404)
    return jsonify(wallet.to_dict())


@app_views.route('/wallets', methods=['POST'], strict_slashes=False)
@token_required
def create_wallet():
    """
    Insert a new wallet into the database
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Data not provided or not JSON"}), 400
    
    try:
        # Create a new wallet object
        if data.get("id"):  # Check if 'id' is provided in data and remove it to prevent conflicts
            data.pop("id")

        wallet = Wallet(**data)
        # Add the wallet to the database session
        # Commit the session to save the wallet to the database
        wallet.save()

        return jsonify({"message": "Wallet created successfully", "wallet": wallet.to_dict()}), 200

    except errors.InvalidTextRepresentation:
        return jsonify({"error": "Invalid data"}), 400

    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


@app_views.route('/wallets/<wallet_id>', methods=['DELETE'], strict_slashes=False)
@token_required
def delete_wallet(wallet_id):
    """Deletes Wallet with a matching wallet_id:
    query-> DELETE FROM wallets WHERE id=wallet_id
    """
    wallet = storage.get(Wallet, id=wallet_id)
    if wallet is None:
        abort(404)
    storage.delete(wallet)
    storage.save()
    return jsonify({"message": "wallet {} deleted successfully".format(wallet.id)}), 200

@app_views.route('/wallets/<wallet_id>/deposit', methods=['POST'], strict_slashes=False)
@token_required
def deposit(wallet_id):
    """
    Deposit funds into a wallet
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data not provided or not json"}), 400
    
    amount = data.get('amount')
    if not amount or amount <= 0:
        return jsonify({"error": "Amount not provided"}), 400

    wallet = storage.get(Wallet, id=wallet_id)
    if not wallet:
        abort(404)
    
    wallet.deposit(amount)
    return jsonify({"message": "Deposit successful", 
                    "wallet": wallet.to_dict()}), 200


@app_views.route('/wallets/<wallet_id>/withdraw', methods=['POST'], strict_slashes=False)
@token_required
def withdraw(wallet_id):
    """
    Withdraw funds from a wallet
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data not provided or not a json"}), 400

    amount = data.get('amount')
    if not amount or amount <= 0:
        return jsonify({"error": "Amount not provided"}), 400

    wallet = storage.get(Wallet, id=wallet_id)
    if not wallet:
        abort(404)

    wallet.withdraw(amount)
    return jsonify({"message": "Withdrawal successful",
                    "wallet": wallet.to_dict()}), 200


@app_views.route('/wallets/<wallet_id>/transactions', methods=['GET'])
@token_required
def transactions(wallet_id):
    """
    Get transaction history for a wallet
    """

    transactions = storage.get_all(Transaction, wallet_id=wallet_id)
    if not transactions:
        abort(404)
    return jsonify([t.to_dict() for t in transactions]), 200

@app_views.route('/wallets/<wallet_id>/balance', methods=['GET'])
@token_required
def get_balance(wallet_id):
    """
    Get the balance of a wallet
    """
    wallet = storage.get(Wallet, id=wallet_id)
    if not wallet:
        abort(404)
    return jsonify({"balance": wallet.get_balance()}), 200

@app_views.route('/wallets/<wallet_id>/transfer', methods=['POST'])
@token_required
def transfer(wallet_id):
    """
    Transfer funds between wallets
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data not provided or not a json"}), 400
    recipient_id = data.get('recipient_id')
    if not recipient_id:
        return jsonify({"error": "Recipient id not provided"}), 400
    recipient = storage.get(Wallet, id=recipient_id)
    if not recipient:
        return jsonify({"error": "Recipient wallet not found"}), 404
    amount = data.get('amount')
    if not amount or amount <= 0:
        return jsonify({"error": "Amount not provided"}), 400
    wallet = storage.get(Wallet, id=wallet_id)
    if not wallet:
        abort(404)
    try:
        print("im here")
        wallet.transfer(amount, recipient_id)
        return jsonify({"message": f"Transfer of {amount} to {recipient_id} was successful",
                            "My wallet": wallet.to_dict()}), 200
    except AssertionError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500
        
