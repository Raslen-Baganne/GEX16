# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    """Crée et configure l'application Flask."""
    app = Flask(__name__)
    app.config.from_object(Config)
    logger.info("Flask app created with config loaded")

    # Initialisation de CORS
    CORS(app, resources={ 
        r"/api/*": { 
            "origins": ["http://localhost:3000"], 
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], 
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True 
        } 
    })
    logger.info("CORS initialized")

    @app.after_request
    def after_request(response):
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response

    # Configuration JWT
    app.config["JWT_SECRET_KEY"] = "your-secret-key-change-it"  # Change this en production !
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600  # 1 heure
    logger.info("JWT configured")

    # Initialisation des extensions
    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)
    logger.info("Extensions (DB, JWT, Migrate) initialized")

    # Initialisation de l'API avec Swagger
    api = Api(app, title="API Auth", version="1.0", description="API d'authentification")
    logger.info("API initialized with Swagger")

    # Importation et enregistrement des Blueprints
    from app.controllers.file_controller import file_blueprint
    from app.controllers.user_folders import user_folders_blueprint
    
    app.register_blueprint(file_blueprint)
    app.register_blueprint(user_folders_blueprint)
    logger.info("File and User Folders blueprints registered")

    # Importation et enregistrement des Namespaces pour Flask-RESTx
    from app.controllers.user_controller import ns as user_ns
    from app.controllers.auth_controller import auth_ns
    from app.controllers.folder_controller import ns as folder_ns

    api.add_namespace(user_ns, path="/api/users")
    api.add_namespace(auth_ns, path="/api/auth")
    api.add_namespace(folder_ns, path="/api/folders")
    
    # Ne pas enregistrer le namespace user_folder_ns pour éviter les conflits
    # avec le blueprint user_folder_blueprint
    # from app.controllers.user_folder_controller import ns as user_folder_ns
    # api.add_namespace(user_folder_ns, path="/api/user-folder")
    logger.info("API namespaces registered")

    return app