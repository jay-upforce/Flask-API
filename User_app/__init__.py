from flask import Blueprint
user_bp = Blueprint('user_bp', __name__, url_prefix='/')

from Entry_app import views, models