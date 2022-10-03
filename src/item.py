from __future__ import annotations


class Item:
    name = None
    url = None
    quantity = None
    price = None

    def __init__(self, name: str, url: str, price: float, quantity: int) -> None:
        self.name = name
        self.url = url
        self.quantity = quantity
        self.price = price

    @property
    def total_price(self) -> float:
        return round(self.price * self.quantity, 2)

    def __str__(self) -> str:
        return f'Product: {self.name} | {self.quantity}x -> {self.price}$ = {self.total_price}$'

    def __repr__(self) -> str:
        return self.__str__()

    def __mul__(self, multiplier: int) -> Item:
        return Item(self.name, self.url, self.price, self.quantity * multiplier)

    @staticmethod
    def header() -> list:
        return [attr for attr in dir(Item)
                if not attr.startswith('__') and attr != 'header']


if __name__ == '__main__':
    item = Item('name', 'url', 1.00, 5)
    print(item)
    print(item.total_price)
    print(Item.header())
    print(item * 2)
