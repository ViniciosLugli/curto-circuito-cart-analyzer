import json
import mechanicalsoup
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


class CCLinks:
    links_file_path = None
    items_data = None
    boleto = True
    HTML_SELECTORS = {
        "PRICE_BOLETO": '#product_addtocart_form > div > div.product-right.col-sm-10 > div:nth-child(3) > span',
        "PRICE_CARD": '[id^=product-price-] > span',
        "PRODUCT_NAME": '#product_addtocart_form > div > div.product-left.col-sm-14 > div.page-title-wrapper.product > h1 > span'
    }

    def __init__(self, links_file_path: str) -> None:
        self.links_file_path = links_file_path

    def __read_json(self) -> dict:
        with open(self.links_file_path, 'r') as f:
            return json.load(f)

    def __update_items_data(self, boleto: bool = boleto) -> None:
        scrapped_items = []
        browser = mechanicalsoup.StatefulBrowser()
        for item in self.__read_json()['items']:
            print(f'Getting data from {item["product_url"]}... ', end='')
            browser.open(item['product_url'])
            scrapped_items.append({
                'product_name': browser.get_current_page().select_one(self.HTML_SELECTORS['PRODUCT_NAME']).text,
                'product_url': item['product_url'],
                'product_price_value': float(browser.get_current_page().select_one(self.HTML_SELECTORS['PRICE_BOLETO' if boleto else 'PRICE_CARD']).text.replace('R$', '').replace(',', '.').strip()),
                'qty': item['qty']
            })
            print(f'Scrapped!\n')
        self.items_data = scrapped_items

    @property
    def links(self) -> list:
        return self.__read_links()

    @property
    def as_cart(self) -> Cart:
        if self.items_data is None:
            self.__update_items_data()

        return Cart([Item(item['product_name'], item['product_url'], item['product_price_value'], item['qty']) for item in self.items_data])


if __name__ == '__main__':
    ccjson = CCJson('data/cart_example.json')
    print('Items:')
    for item in ccjson.items:
        print(f'\t{item}')

    cclinks = CCLinks('data/items_raw_example.json')
    print('Links:')
    for link in cclinks.links:
        print(f'\t{link}')
