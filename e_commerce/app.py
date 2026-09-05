import uuid

from flask import Flask, request
from db import shops, products
app = Flask(__name__)

## get shop data
@app.route('/shops',methods=['GET'])
def get_shops():
    return {"shops": list(shops.values())}, 200

## add shops
@app.route('/shop', methods=['POST'])
def create_shop():
    shop_data = request.json
    shop_id = uuid.uuid4().hex
    shop = {**shop_data, "id": shop_id}
    shops[shop_id] = shop
    return shop
def get_shops():
    return shops

@app.route("/product", methods=["POST"])
def create_product(shop_name):
    new_product = request.json
    if new_product["shop_id"] not in shops:
        return {"message": "Shop Not Found"}, 404
    product_id = uuid.uuid4().hex
    product = {**new_product, "id": product_id}
    products[product_id] = product
    return product

  
@app.route("/shop/<shop_id>", methods=["GET"])
def get_shop(shop_id):
    try:
        return shops[shop_id]
    except KeyError:
    
     return {"message": "Shop not found"}, 404



## get products
@app.route('/products',methods=['GET'])
def get_products():
    return {"products": list(products.values())}, 200

## get products id

@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    try:
        return products[product_id]
    except KeyError:
    
     return {"message": "Product not found"}, 404
## delete products
@app.route("/products/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        del products[product_id]
    except:
        return {"messages": "Products not found"}, 404

## update products
@app.route("/products/<product_id>", methods=["UPDATE"])
def update_product(product_id):
    product_data = request.json
    if "price" not in product_data or "name" not in product_data:
                return {"messages": "Please Ensure name and price are include"}, 400
    try:
        products = products[product_id]
        ## merge two dictionaries 
        products |= product_data
        return products
    except KeyError:
                return {"messages": "Products not found"}, 404



app.run()