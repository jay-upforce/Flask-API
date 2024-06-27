from flask import request, jsonify
from marshmallow import ValidationError
from app import db
from Competition_app import competition_bp      # import blueprint from init file
from Competition_app.models import Competition
from Competition_app.schemas import CompetitionSerializer


@competition_bp.route('/', methods=['POST'])    # 'http://127.0.0.1:5000/competition' route with POST http method
def create_competition():
    try:
        data = request.get_json()   # get data
        validate_data = CompetitionSerializer().load(data)  # check data validation
    except ValidationError as e:    # when user's enter invalid data format then occuer exception
        return jsonify({'error': str(e)}), 400  # return Error msg response with convert in into json 
    
    competition = Competition(**validate_data)  # add dict into Competition table

    db.session.add(competition) # add data into db
    db.session.commit() # save changes

    return jsonify({"message": "Competition Created.",
                    "data": CompetitionSerializer().dump(competition)}), 201    # return success msg response with convert in into json


@competition_bp.route('/', methods=['GET'])     # 'http://127.0.0.1:5000/competition' route with GET http method
def get_competitions():
    competitions = Competition.query.filter_by(is_delete=False).all()   # get all records where is_delete=False from competition table 
    return jsonify(CompetitionSerializer(many=True).dump(competitions)), 200    # return success msg response with convert in into json


@competition_bp.route('/<int:id>', methods=['GET'])     # 'http://127.0.0.1:5000/competition/<id>' route with GET http method
def get_competition(id):
    competition = Competition.query.get_or_404(id)  # get competition object where id = id of competition table
    if competition.is_delete:   # check if column is_delete is True or False of competition table
        return jsonify({"message": "Competition not found"}), 404   # return Error msg response with convert in into json 
    return jsonify(CompetitionSerializer().dump(competition)), 200  # return success msg response with convert in into json


@competition_bp.route('/<int:id>', methods=['PATCH'])       # 'http://127.0.0.1:5000/competition/<id>' route with PATCH http method
def update_competition(id):
    competition = Competition.query.get_or_404(id)  # get competition object where id = id of competition table
    if competition.is_delete:   # check if column is_delete is True or False of competition table
        return jsonify({"message": "Competition not found"}), 404   # return Error msg response with convert in into json 

    data = request.get_json()   # get data

    try:
        validated_data = CompetitionSerializer().load(data, partial=True)   # check data validation
    except ValidationError as e:    # when user's enter invalid data format then occuer exception
        return jsonify({'error': str(e)}), 400  # return Error msg response with convert in into json 
    
    # update competition table column
    competition.title = validated_data.get('title', competition.title)  # get title if name not found than get existing title
    competition.social_issue = validated_data.get('social_issue', competition.social_issue) # get social_issue if name not found than get existing social_issue
    competition.user_id = validated_data.get('user_id', competition.user_id)    # get user_id if name not found than get existing user_id
    competition.is_active = validated_data.get('is_active', competition.is_active)  # get is_active if name not found than get existing is_active

    db.session.commit() # save changes
    return jsonify(CompetitionSerializer().dump(competition)), 200  # return success msg response with convert in into json


@competition_bp.route('/<int:id>', methods=['DELETE'])      # 'http://127.0.0.1:5000/competition/<id>' route with DELETE http method
def delete_competition(id):
    competition = Competition.query.get_or_404(id)  # get competition object where id = id of competition table
    if competition.is_delete:   # check if column is_delete is True or False of competition table
        return jsonify({"message": "Competition not found"}), 404   # return Error msg response with convert in into json 

    competition.is_delete = True    # update is_delete column False to True in competition table
    db.session.commit() # save changes
    return jsonify({"message": "Competition deleted successfully"}), 200    # return success msg response with convert in into json