from analyzer import CCJson
from exporter import Exporter

cart = CCJson('data/cart_example.json').as_cart
Exporter.to_csv(cart)
Exporter.to_json(cart)
