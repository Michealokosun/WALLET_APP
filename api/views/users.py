#!/usr/bin/env python
"""
users route controller for handling api calls for User"""

from sqlalchemy.exc import SQLAlchemyError
from api.views import app_views
from flask import jsonify, request, abort, session
from psycopg2 import errors
import psycopg2
from models.user import User
from models import storage
from api.views.utils.token_required import token_required
from api.views.utils.jwt_token import create_jwt_token, decode_jwt_token


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """
    query-> SELECT * FROM users 
    [Returns a dictionary (key:obj) object for easy indexing]
    """
    users = storage.get_all(User)
    if not users:
        abort(404)
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@token_required
def get_user_by_id(user_id):
    """
    query-> SELECT * FROM user where id=user_id
    Returns a user object
    """
    
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
    Insert a new user into the database
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Data not provided or not JSON"}), 400
    
    user = storage.get(User, email=data['email'])
    if user:
        return jsonify({"error": "User already exists"}), 400

    try:
        # Create a new user object
        if data.get("id"):  # Check if 'id' is provided in data and remove it to prevent conflicts
            data.pop("id")

        user = User(**data)
        # Add the user to the database session
        # Commit the session to save the user to the database
        user.save()

        return jsonify({"message": "User created successfully", "user": user.to_dict()}), 200

    except errors.InvalidTextRepresentation:
        return jsonify({"error": "Invalid data"}), 400

    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@token_required
def update_user(user_id):
    """Update User with a matching user_id"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'error': 'Data not a JSON'}), 400
    if 'id' in data:
        data.pop('id')
    if 'password' in data:
        data.pop('password')
    try:
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict()), 200
    except errors.UniqueViolation:
        return jsonify({"error": "User already exists"}), 400

    except errors.InvalidTextRepresentation:
        return jsonify({"error": "Invalid data"}), 400

    except SQLAlchemyError as e:
        print(e)
        return jsonify({"error": "Database error", "details": str(e)}), 500

    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
@token_required
def delete_user(user_id):
    """Deletes User with a matching user_id:
    query-> DELETE FROM users WHERE id=user_id
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({"message": "user {} deleted successfully".format(user.email)}), 200


@app_views.route('/login', methods=['POST'])
# @token_required
def login():
    # Get the user object based on credentials
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Data not provided or not JSON"})
    user = storage.get(User, email=data['email'])
    if not user:
        return abort(404, {"error": "User not found"})
    if not user.check_password(data['password']):
        return abort(401, {"error": "Invalid password"})
    token  = create_jwt_token(user.id)
    response = jsonify({"token": token, "user": user.to_dict()})
    response.headers['Authorization'] = f"Bearer {token}"
    return response, 200
        
@app_views.route('/logout', methods=['GET'])
@token_required
def logout():
    return jsonify({"message": "User logged out"}), 200


@app_views.route('/users/me', methods=['GET'])
@token_required
def get_current_user():
    """
    Returns the user object of the currently logged in user
    """
    # token = decode_jwt_token(request.headers.get('Authorization'))
    # if not token:
    #     abort(401)
    # print("user_id :", user_id)
    # user = storage.get(User, user_id)
    # if not user:
    #     abort(404)
    return "it have passed"