from flask import Blueprint
entry_bp = Blueprint('entry', __name__, url_prefix='/entry')

from Entry_app import views, models