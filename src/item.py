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
        return self.price * self.quantity

    def __str__(self) -> str:
        return f'Product: {self.name} | {self.quantity}x -> {self.price}$ = {self.total_price}$'


if __name__ == '__main__':
    item = Item('name', 'url', 1.00, 5)
    print(item)
    print(item.total_price)
