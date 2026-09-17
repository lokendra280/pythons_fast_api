from flask import request
import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import products
from schemas import ProductSchema, ProductUpdateSchema
blueprint = Blueprint("product", __name__, description= "Operations on product")


@blueprint.route("/products/<product_id>")

class Shop(MethodView):
    @blueprint.response(200, ProductSchema)
    def get(self, product_id):
        try:
            return products[product_id]
        except KeyError:
            abort(404, message="Product not found")
@blueprint.arguments(ProductUpdateSchema)         
@blueprint.arguments(200,ProductSchema)

def put(self,product_data, product_id):

        try:
            product = products[product_id]
            product |= product_data
            return product
        except KeyError:
            abort(404, message="Product not found")

def delete(self, product_id):
        try:
            del products[product_id]
            return {"message": "Product deleted"}
        except KeyError:
            abort(404, message="Product not found")


@blueprint.route("/product")
class ProductList(MethodView):
    @blueprint.arguments(200, ProductSchema(many= True))

    def get(self):
        return {"products": list(products.values())}, 200

@blueprint.arguments(ProductSchema)
@blueprint.arguments(201, ProductSchema)
def post(self, new_product):

        for product in products.values():
            if (
                new_product["name"] == product["name"]
                and new_product["shop_id"] == product["shop_id"]
            ):
                abort(400, message="Product already exists")

        product_id = uuid.uuid4().hex
        product = {**new_product, "id": product_id}
        products[product_id] = product
        return product