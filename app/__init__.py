from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app(config_class=None):
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "super-secret-key-neon-ai-2026"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///timetable.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    # IMPORTANT: Import models BEFORE creating tables
    from app.models import (
        User,
        Department,
        Faculty,
        BlockedTimeSlot,
        Subject,
        Room,
        Section,
        Course,
        CourseSession,
        TimeSlot,
        Timetable,
        TimetableEntry,
    )

    with app.app_context():
        db.create_all()

    from app.routes.main import main_bp
    from app.routes.api import api_bp
    from app.routes.search import search_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(search_bp, url_prefix="/api/search")
    app.register_blueprint(admin_bp)

    return app