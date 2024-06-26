from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from User_app import db
from Competition_app.models import Competition
from Competition_app.schemas import CompetitionSerializer

competition_bp = Blueprint('competition_bp', __name__, url_prefix='/competition')

@competition_bp.route('/', methods=['POST'])
def create_competition():
    try:
        data = request.get_json()
        validate_data = CompetitionSerializer().load(data)
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    
    competition = Competition(**validate_data)
    db.session.add(competition)
    db.session.commit()
    return jsonify({"message": "Competition Created.",
                    "data": CompetitionSerializer().dump(competition)}), 201

"""
@competition_bp.route('/', methods=['GET'])
def get_competitions():
    competitions = Competition.query.filter_by(is_delete=False).all()
    return competitions_schema.jsonify(competitions), 200

@competition_bp.route('/<int:id>', methods=['GET'])
def get_competition(id):
    competition = Competition.query.get_or_404(id)
    if competition.is_delete:
        return jsonify({"message": "Competition not found"}), 404
    return competition_schema.jsonify(competition), 200

@competition_bp.route('/<int:id>', methods=['PUT'])
def update_competition(id):
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    competition = Competition.query.get_or_404(id)
    if competition.is_delete:
        return jsonify({"message": "Competition not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    errors = competition_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    competition.title = data.get('title', competition.title)
    competition.social_issue = data.get('social_issue', competition.social_issue)
    competition.user_id = data.get('user_id', competition.user_id)
    competition.is_active = data.get('is_active', competition.is_active)
    
    db.session.commit()
    return competition_schema.jsonify(competition), 200

@competition_bp.route('/<int:id>', methods=['DELETE'])
def delete_competition(id):
    competition = Competition.query.get_or_404(id)
    if competition.is_delete:
        return jsonify({"message": "Competition not found"}), 404

    competition.is_delete = True
    db.session.commit()
    return jsonify({"message": "Competition deleted successfully"}), 200
"""