from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app import db
from .models import User
from .schemas import UserSerializer


user_bp = Blueprint('user_bp', __name__, url_prefix='/')

@user_bp.route('/user', methods=['POST'])   # 'http://127.0.0.1:5000/user' route with POST http method
def create_user():
    try:
        data = request.get_json()   # get data 
        validated_data = UserSerializer().load(data)  # check data validation
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400  

    user = User(**validated_data)   # make new user data dict

    db.session.add(user)    # add data into db
    db.session.commit()     # save changes

    return jsonify({'message': 'User created successfully', 
                    'data': UserSerializer().dump(user)}), 201  # return response with convert in into json


@user_bp.route('/user', methods=['GET'])    # 'http://127.0.0.1:5000/user' route with GET http method
def get_users():
    users = User.query.filter_by(is_delete=False).all() # get all records from table 
    return jsonify(UserSerializer(many=True).dump(users)), 200  # return response with convert in into json


@user_bp.route('/user/<int:id>', methods=['GET'])   # 'http://127.0.0.1:5000/user/<id>' route with GET http method
def get_user(id):
    user = User.query.get_or_404(id)    # get user object where id = id
    if user.is_delete:  # check if user column is_delete is Not None
        return jsonify({"message": "User not found"}), 404     # return response with convert in into json
    return jsonify(UserSerializer().dump(user)), 200    # return response with convertin into json


@user_bp.route('/user/<int:id>', methods=['PATCH']) # 'http://127.0.0.1:5000/user/<id>' route with PATCH http method
def update_user(id):
    user = User.query.get_or_404(id)    # get user object where id = id
    if user.is_delete:  # check if user column is_delete is Not None
        return jsonify({"message": "User not found"}), 404     # return response with convert in into json

    data = request.get_json()   # get data 

    user.name = data.get('name', user.name)
    user.gender = data.get('gender', user.gender)
    user.phone_number = data.get('phone_number', user.phone_number)
    user.is_active = data.get('is_active', user.is_active)

    try:
        validated_data = UserSerializer().load(data, partial=True)  # check data validation
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400  

    db.session.commit()
    return jsonify(UserSerializer().dump(user)), 200


@user_bp.route('/user/<int:id>', methods=['DELETE'])    # 'http://127.0.0.1:5000/user/<id>' route with DELETE http method
def delete_user(id):
    user = User.query.get_or_404(id)    # get user object where id = id
    if user.is_delete:  # check if user column is_delete is Not None
        return jsonify({"message": "User not found"}), 404     # return response with convert in into json

    user.is_delete = True
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200