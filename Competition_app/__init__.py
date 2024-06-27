from flask import Blueprint
competition_bp = Blueprint('competition_bp', __name__, url_prefix='/competition')

from Competition_app import views, models