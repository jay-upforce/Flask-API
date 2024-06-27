from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from User_app import user_bp
from app import db
from .models import User
from .schemas import UserSerializer


@user_bp.route('/user', methods=['POST'])   # 'http://127.0.0.1:5000/user' route with POST http method
def create_user():
    try:
        data = request.get_json()   # get data 
        validated_data = UserSerializer().load(data)  # check data validation
    except ValidationError as e:    # when user's enter invalid data format then occuer exception
        return jsonify({'error': str(e)}), 400  # return Error msg response with convert in into json 

    user = User(**validated_data)   # add dict into User table

    db.session.add(user)    # add data into db
    db.session.commit()     # save changes

    return jsonify({'message': 'User created successfully', 
                    'data': UserSerializer().dump(user)}), 201  # return success msg response with convert in into json


@user_bp.route('/user', methods=['GET'])    # 'http://127.0.0.1:5000/user' route with GET http method
def get_users():
    users = User.query.filter_by(is_delete=False).all() # get all records where is_delete=False from user table 
    return jsonify(UserSerializer(many=True).dump(users)), 200  # return success msg response with convert in into json


@user_bp.route('/user/<int:id>', methods=['GET'])   # 'http://127.0.0.1:5000/user/<id>' route with GET http method
def get_user(id):
    user = User.query.get_or_404(id)    # get user object where id = id of user table
    if user.is_delete:  # check if column is_delete is True or False of users table
        return jsonify({"message": "User not found"}), 404     # return Error msg response with convert in into json
    return jsonify(UserSerializer().dump(user)), 200    # return success msg response with convert in into json


@user_bp.route('/user/<int:id>', methods=['PATCH'])     # 'http://127.0.0.1:5000/user/<id>' route with PATCH http method
def update_user(id):
    user = User.query.get_or_404(id)    # get user object where id = id of user table
    if user.is_delete:  # check if column is_delete is True or False of users table
        return jsonify({"message": "User not found"}), 404     # return Error msg response with convert in into json

    data = request.get_json()   # get data 

    try:
        validated_data = UserSerializer().load(data, partial=True)  # check data validation
    except ValidationError as e:    # when user's enter invalid data format then occuer exception
        return jsonify({'error': str(e)}), 400  # return Error msg response with convert in into json
    
    # update user table column
    user.name = validated_data.get('name', user.name)   # get name if name not found than get existing name
    user.gender = validated_data.get('gender', user.gender) # get gender if name not found than get existing gender
    user.phone_number = validated_data.get('phone_number', user.phone_number)   # get phone_number if name not found than get existing phone_number
    user.is_active = validated_data.get('is_active', user.is_active)    # get is_active if name not found than get existing is_active

    db.session.commit() # save changes
    return jsonify(UserSerializer().dump(user)), 200    # return success msg response with convert in into json


@user_bp.route('/user/<int:id>', methods=['DELETE'])    # 'http://127.0.0.1:5000/user/<id>' route with DELETE http method
def delete_user(id):
    user = User.query.get_or_404(id)    # get user object where id = id of user table
    if user.is_delete:  # check if column is_delete is True or False of users table
        return jsonify({"message": "User not found"}), 404     # return Error msg response with convert in into json

    user.is_delete = True   # update is_delete column False to True in user table
    db.session.commit() # save changes
    return jsonify({"message": "User deleted successfully"}), 200   # return success msg response with convert in into json