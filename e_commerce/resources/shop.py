from urllib import request
import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import shops
from schemas import ShopSchema

blueprint = Blueprint("shops", __name__, description= "Operations on shops")

@blueprint.route("/shop/<shop_id>")
class Shop(MethodView):
    @blueprint.argument(200, ShopSchema)
    def get (self, shop_id):
        try:
            return shops[shop_id]
        except KeyError:
            abort(404, message="Shop not found")


def delete(self, shop_id):
    try:
        del shops[shop_id]
        return {"message": "shop deleted"}
    except KeyError:
        abort(404, message="Shop not found")

@blueprint.route("/shop")

class ShopList(MethodView):
    @blueprint.argument(200, ShopSchema(many = True))

    def get (self):
            return {"shops": list(shops.values())}, 200

@blueprint.arguments(ShopSchema)
@blueprint.argument(201, ShopSchema)

def post(self,shop_data):
      
            for shop in shops.values():
                 if shop_data["name"] == shop["name"]:
                                      abort(400, message="Shop already exits")

            shop_id = uuid.uuid4().hex
            shop = {**shop_data, "id": shop_id}
            shops[shop_id] = shop
            return shop