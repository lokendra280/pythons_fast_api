from marshmallow import Schema, fields

class PlainProductSchema(Schema):
    id = fields.Str(dump_only = True)
    name = fields.Str(dump_only = True)
    price = fields.Float(dump_only = True)

class PlainShopSchema(Schema):
    id = fields.Str(dump_only = True)
    price = fields.Float(dump_only = True)


class ProductSchema(PlainProductSchema):
    shop_id = fields.Str(dump_only = True)
    shop = fields.Nested(PlainShopSchema(), dump_only= True)
class ProductUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ShopSchema(Schema):
   product = fields.List(fields.Nested(PlainProductSchema()), dump_only= True)