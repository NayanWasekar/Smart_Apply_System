from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db  # imports all models automatically

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init DB + Migrations
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes/blueprints
    from routes.auth_routes import auth_bp
    from routes.hr_routes import hr_bp
    from routes.job_routes import job_bp
    from routes.application_routes import application_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(hr_bp)
    app.register_blueprint(job_bp)
    app.register_blueprint(application_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
