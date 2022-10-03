from item import Item
from cart import Cart
from datetime import datetime
import json


class Manager:
    def __init__(self, filename) -> None:
        self.filename = filename

    def save_to_file(self, cart) -> None: pass


class CsvManager(Manager):
    def __init__(self, filename) -> None:
        super().__init__(filename)

    def save_to_file(self, cart) -> None:
        with open(self.filename, 'w') as f:
            header = Item.header()
            f.write(",".join(header))
            for item in cart.items:
                attributes = [str(getattr(item, attr)) for attr in header]
                attributes = [attr.replace(',', '.') for attr in attributes]
                line = ",".join(attributes)
                f.write(f'\n{line}')

            f.write(f'\n\nTotal: ${cart.total_price}')


class JsonManager(Manager):
    def __init__(self, filename) -> None:
        super().__init__(filename)

    def save_to_file(self, cart) -> None:
        header = Item.header()
        json_output = {}
        for idx, item in enumerate(cart.items):
            attributes = [str(getattr(item, attr)) for attr in header]
            json_output[idx] = dict(zip(header, attributes))
        json_output['total'] = f'${cart.total_price}'
        with open(self.filename, 'w') as f:
            json.dump(json_output, f, indent=4)


class Exporter:
    def generate_filename() -> str:
        return f'cart_{datetime.now().strftime("%d%m%Y%H%M%S")}'

    def to_csv(cart: Cart) -> None:
        CsvManager(f'{Exporter.generate_filename()}.csv').save_to_file(cart)

    def to_json(cart: Cart) -> None:
        JsonManager(f'{Exporter.generate_filename()}.json').save_to_file(cart)


if __name__ == '__main__':
    cart = Cart()
    cart.add(Item('name1', 'url1', 1.00, 5))
    cart.add(Item('name2', 'url2', 4.00, 2))
    cart.add(Item('name3', 'url3', 6.00, 3))

    Exporter.to_csv(cart)
    Exporter.to_json(cart)
