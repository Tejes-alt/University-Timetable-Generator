from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app(config_class=None):
    app = Flask(__name__)
    
    # Basic configuration
    app.config['SECRET_KEY'] = 'super-secret-key-neon-ai-2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timetable.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.routes.main import main_bp
    from app.routes.api import api_bp
    from app.routes.search import search_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(search_bp, url_prefix='/api/search')

    from app.routes.admin import admin_bp
    app.register_blueprint(admin_bp)

    return app
