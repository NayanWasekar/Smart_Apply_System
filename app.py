from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from models import db
from routes import register_routes  # ✅ import the central route registrar

# Extensions
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Enable CORS (React dev + prod)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})

    # Register all routes
    register_routes(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
