from analyzer import CCJson, CCLinks
from exporter import Exporter


def test_ccjson() -> None:
    cart = CCJson('data/cart_example.json').as_cart
    cart = cart * 10

    Exporter.to_csv(cart)
    Exporter.to_json(cart)

#


def test_cclinks() -> None:
    cart = CCLinks('data/items_raw_example.json').as_cart

    cart = cart * 10

    Exporter.to_csv(cart)
    Exporter.to_json(cart)


if __name__ == '__main__':
    test_ccjson()
    test_cclinks()
