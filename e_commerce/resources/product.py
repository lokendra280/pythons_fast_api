from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from schemas import ProductSchema, ProductUpdateSchema
from models import ProductModel
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from flask_jwt_extended import jwt_required

blueprint = Blueprint(
    "product",
    __name__,
    description="Operations on product"
)


@blueprint.route("/products/<product_id>")
class Shop(MethodView):
    @jwt_required(fresh= True)
    @blueprint.response(200, ProductSchema)
    def get(self, product_id):
        product = ProductModel.query.get_or_404(product_id)
        return product
    @jwt_required(fresh= True)
    @blueprint.arguments(ProductUpdateSchema)
    @blueprint.response(200, ProductSchema)
    def put(self, product_data, product_id):
        product = ProductModel.query.get_or_404(product_id)

        product.price = product_data["price"]
        product.name = product_data["name"]

        try:
            db.session.add(product)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error while updating product")

        return product
    @jwt_required(fresh= True)
    @blueprint.response(200)
    def delete(self, product_id):
        product = ProductModel.query.get_or_404(product_id)

        db.session.delete(product)

        try:
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error while deleting the product")

        return {"message": "Product deleted"}


@blueprint.route("/product")
class ProductList(MethodView):
    @jwt_required(fresh= True)
    @blueprint.response(200, ProductSchema(many=True))
    def get(self):
        return ProductModel.query.all()
    @jwt_required(fresh= True)
    @blueprint.arguments(ProductSchema)
    @blueprint.response(201, ProductSchema)
    def post(self, new_product):
        product = ProductModel(**new_product)

        try:
            db.session.add(product)
            db.session.commit()
        except IntegrityError:
                    db.session.rollback()
                    abort(400, message="A Product with that name already exists")
        
        except SQLAlchemyError:
            abort(
                500,
                message="An error occurred while inserting the product"
            )

        return product