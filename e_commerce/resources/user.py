from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)

from db import db
from models import UserModel
from schemas import UserSchema
from blacklist import BlackList


blueprint = Blueprint(
    "Users",
    "users",
    description="Operations on users"
)


# =========================
# REGISTER
# =========================

@blueprint.route("/register")
class UserRegister(MethodView):

    @blueprint.arguments(UserSchema)
    def post(self, user_data):

        existing_user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if existing_user:
            abort(
                409,
                message="A user with this username already exists."
            )

        hashed_password = pbkdf2_sha256.hash(
            user_data["password"]
        )

        user = UserModel(
            username=user_data["username"],
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return {
            "message": "User created successfully"
        }, 201


# =========================
# GET USER
# =========================

@blueprint.route("/user/<int:user_id>")
class User(MethodView):

    @blueprint.response(200, UserSchema)
    def get(self, user_id):

        user = UserModel.query.get_or_404(user_id)

        return user


# =========================
# LOGIN
# =========================

@blueprint.route("/login")
class UserLogin(MethodView):

    @blueprint.arguments(UserSchema)
    def post(self, user_data):

        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        # User doesn't exist
        if not user:
            abort(
                401,
                message="Invalid username or password."
            )

        # Password is incorrect
        if not pbkdf2_sha256.verify(
            user_data["password"],
            user.password
        ):
            abort(
                401,
                message="Invalid username or password."
            )

        # Create access token
        access_token = create_access_token(
            identity=str(user.id),
            fresh=True
        )

        # Create refresh token
        refresh_token = create_refresh_token(
            identity=str(user.id)
        )

        return {
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": refresh_token
        }, 200


# =========================
# LOGOUT
# =========================

@blueprint.route("/logout")
class UserLogout(MethodView):

    @jwt_required()
    def delete(self):

        jti = get_jwt()["jti"]

        BlackList.add(jti)

        return {
            "message": "Successfully logged out"
        }, 200


# =========================
# REFRESH TOKEN
# =========================

@blueprint.route("/refresh")
class UserRefresh(MethodView):

    @jwt_required(refresh=True)
    def post(self):

        current_user = get_jwt_identity()

        new_access_token = create_access_token(
            identity=str(current_user),
            fresh=False
        )

        return {
            "access_token": new_access_token
        }, 200