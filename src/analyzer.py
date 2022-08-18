import json
import re
from item import Item
from cart import Cart


class CCJson:
    json_file_path = None

    def __remove_ilegal_chars(self, string: str) -> str:
        return re.sub(r'[^a-zA-Z0-9_\- ]', '', string)

    def __init__(self, json_file_path: str) -> None:
        self.json_file_path = json_file_path

    def __read_json(self) -> dict:
        with open(self.json_file_path, 'r') as f:
            return json.load(f)

    def __json_item_to_object(self, json_item: dict) -> Item:
        return Item(self.__remove_ilegal_chars(str(json_item['product_name'])), str(json_item['product_url']), round(float(json_item['product_price_value']), 2), int(json_item['qty']))

    def __get_json_items(self) -> list:
        return self.__read_json()['items']

    @property
    def items(self) -> list:
        return [self.__json_item_to_object(item) for item in self.__get_json_items()]

    @property
    def as_cart(self) -> Cart:
        return Cart(self.items)


if __name__ == '__main__':
    ccjson = CCJson('data/cart_example.json')
    print('Items:')
    for item in ccjson.items:
        print(f'\t{item}')
