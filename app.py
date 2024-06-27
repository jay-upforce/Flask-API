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
    
    # Register blueprints routes
    from User_app.views import user_bp
    app.register_blueprint(user_bp, url_prefix='/')     # resgiter User_app blueprint route
    
    from Competition_app.views import competition_bp
    app.register_blueprint(competition_bp, url_prefix='/competition')    # register Competition_app blueprint route

    from Entry_app.views import entry_bp
    app.register_blueprint(entry_bp, url_prefix='/entry')       # register Entry_app blueprint route

    return app

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
