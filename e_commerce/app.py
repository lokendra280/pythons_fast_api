import os

from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db
import models

from resources.product import blueprint as productBluePrint
from resources.shop import blueprint as shopBluePrint
from resources.user import blueprint as userBluePrint
from blacklist import BlackList


app = Flask(__name__)


# =========================
# Flask-Smorest
# =========================

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Shops Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"

app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = (
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
)


# =========================
# Database
# =========================

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:///shop.db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# =========================
# JWT
# =========================

app.config["JWT_SECRET_KEY"] = os.getenv(
    "JWT_SECRET_KEY",
    "learn_with_prapat"
)

jwt = JWTManager(app)


# =========================
# JWT Blocklist
# =========================

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):

    return jwt_payload["jti"] in BlackList


# =========================
# Expired Token
# =========================

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):

    return (
        jsonify({
            "message": "The provided token is expired",
            "error": "token_expired"
        }),
        401
    )


# =========================
# Revoked Token
# =========================

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):

    return (
        jsonify({
            "message": "The token has been revoked",
            "error": "token_revoked"
        }),
        401
    )


# =========================
# Fresh Token Required
# =========================

@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):

    return (
        jsonify({
            "message": "The token is not fresh",
            "error": "fresh_token_required"
        }),
        401
    )


# =========================
# Invalid Token
# =========================

@jwt.invalid_token_loader
def invalid_token_callback(error):

    return (
        jsonify({
            "message": "Signature verification failed",
            "error": "invalid_token"
        }),
        401
    )


# =========================
# Missing Token
# =========================

@jwt.unauthorized_loader
def missing_token_callback(error):

    return (
        jsonify({
            "message": "Request does not contain a valid access token",
            "error": "authorization_required"
        }),
        401
    )


# =========================
# Create Database Tables
# =========================

with app.app_context():
    db.create_all()


# =========================
# Flask-Smorest API
# =========================

api = Api(app)


# =========================
# Register Blueprints
# =========================

api.register_blueprint(productBluePrint)
api.register_blueprint(userBluePrint)
api.register_blueprint(shopBluePrint)