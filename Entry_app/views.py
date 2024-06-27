from flask import request, jsonify
from marshmallow import ValidationError
from app import db
from Entry_app import entry_bp      # import blueprint from init file
from Entry_app.models import Entry
from Entry_app.schemas import EntrySerializer


@entry_bp.route('/', methods=['POST'])    # 'http://127.0.0.1:5000/entry' route with POST http method
def create_entry():
    try:
        data = request.get_json()   # get data
        validate_data = EntrySerializer().load(data)  # check data validation
    except ValidationError as e:    # when user's enter invalid data format then occuer exception
        return jsonify({'error': str(e)}), 400  # return Error msg response with convert in into json 
    
    entry = Entry(**validate_data)  # add dict into Entry table

    db.session.add(entry) # add data into db
    db.session.commit() # save changes

    return jsonify({"message": "Entry Created.",
                    "data": EntrySerializer().dump(entry)}), 201    # return success msg response with convert in into json


@entry_bp.route('/', methods=['GET'])     # 'http://127.0.0.1:5000/entry' route with GET http method
def get_entries():
    entry = Entry.query.filter_by(is_delete=False).all()   # get all records where is_delete=False from entry table 
    return jsonify(EntrySerializer(many=True).dump(entry)), 200    # return success msg response with convert in into json


@entry_bp.route('/<int:id>', methods=['GET'])     # 'http://127.0.0.1:5000/entry/<id>' route with GET http method
def get_entry(id):
    entry = Entry.query.get_or_404(id)  # get entry object where id = id of entry table
    if entry.is_delete:   # check if column is_delete is True or False of entry table
        return jsonify({"message": "Entry not found"}), 404   # return Error msg response with convert in into json 
    return jsonify(EntrySerializer().dump(entry)), 200  # return success msg response with convert in into json


@entry_bp.route('/<int:id>', methods=['PATCH'])       # 'http://127.0.0.1:5000/entry/<id>' route with PATCH http method
def update_entry(id):
    entry = Entry.query.get_or_404(id)  # get entry object where id = id of entry table
    if entry.is_delete:   # check if column is_delete is True or False of competition table
        return jsonify({"message": "Entry not found"}), 404   # return Error msg response with convert in into json 

    data = request.get_json()   # get data

    try:
        validated_data = EntrySerializer().load(data, partial=True)   # check data validation
    except ValidationError as e:    # when user's enter invalid data format then occuer exception
        return jsonify({'error': str(e)}), 400  # return Error msg response with convert in into json 
    
    # update competition table column
    entry.name = validated_data.get('name', entry.name)  # get name if name not found than get existing name
    entry.country = validated_data.get('country', entry.country) # get country if name not found than get existing country
    entry.state = validated_data.get('state', entry.state)    # get state if name not found than get existing state
    entry.how_did_you_hear = validated_data.get('how_did_you_hear', entry.how_did_you_hear)  # get how_did_you_hear if name not found than get existing how_did_you_hear

    entry.competition_id = validated_data.get('competition_id', entry.competition_id)  # get competition_id if name not found than get existing competition_id
    entry.is_entrant_part_of_institution = validated_data.get('is_entrant_part_of_institution', entry.is_entrant_part_of_institution) # get is_entrant_part_of_institution if name not found than get existing is_entrant_part_of_institution
    entry.i_am_part_of = validated_data.get('i_am_part_of', entry.i_am_part_of)    # get i_am_part_of if name not found than get existing i_am_part_of
    entry.is_active = validated_data.get('is_active', entry.is_active)  # get is_active if name not found than get existing is_active


    db.session.commit() # save changes
    return jsonify(EntrySerializer().dump(entry)), 200  # return success msg response with convert in into json


@entry_bp.route('/<int:id>', methods=['DELETE'])      # 'http://127.0.0.1:5000/entry/<id>' route with DELETE http method
def delete_entry(id):
    entry = Entry.query.get_or_404(id)  # get entry object where id = id of entry table
    if entry.is_delete:   # check if column is_delete is True or False of entry table
        return jsonify({"message": "Entry not found"}), 404   # return Error msg response with convert in into json 

    entry.is_delete = True    # update is_delete column False to True in entry table
    db.session.commit() # save changes
    return jsonify({"message": "Entry deleted successfully"}), 200    # return success msg response with convert in into json