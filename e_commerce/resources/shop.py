from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required

from models import ShopModel
from db import db
from schemas import ShopSchema


blueprint = Blueprint(
    "shops",
    __name__,
    description="Operations on shops"
)


@blueprint.route("/shop/<shop_id>")
class Shop(MethodView):
    @jwt_required(fresh= True)
    @blueprint.response(200, ShopSchema)
    def get(self, shop_id):
        shop = ShopModel.query.get_or_404(shop_id)
        return shop
    @jwt_required(fresh= True)
    @blueprint.response(200)
    def delete(self, shop_id):
        shop = ShopModel.query.get_or_404(shop_id)

        db.session.delete(shop)

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="An error occurred while deleting the shop")

        return {"message": "Shop deleted"}


@blueprint.route("/shop")
class ShopList(MethodView):
    @jwt_required(fresh= True)

    @blueprint.response(200, ShopSchema(many=True))
    def get(self):
        return ShopModel.query.all()
    @jwt_required(fresh= True)

    @blueprint.arguments(ShopSchema)
    @blueprint.response(201, ShopSchema)
    def post(self, shop_data):

        shop = ShopModel(**shop_data)

        try:
            db.session.add(shop)
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            abort(400, message="A shop with that name already exists")

        except SQLAlchemyError:
            db.session.rollback()
            abort(
                500,
                message="An error occurred while inserting the shop"
            )

        return shop