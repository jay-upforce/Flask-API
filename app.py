from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Config class
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Initialize the database and migration objects
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database and migrations with the app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints for User and Competition apps
    from User_app.views import user_bp
    app.register_blueprint(user_bp, url_prefix='/') # resgiter user blueprint route
    
    from Competition_app.views import competition_bp
    app.register_blueprint(competition_bp, url_prefix='/competition')    # register competition blueprint route

    return app

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
