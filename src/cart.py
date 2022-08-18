from item import Item
from collections.abc import Generator


class Cart:
    items = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, search_item_mask: Item) -> None:
        finded = False
        for item in self.items:
            for (k, v) in search_item_mask.__dict__.items():
                if v != None and v != item.__dict__[k]:
                    finded = False
                    break
                finded = True

            if finded:
                self.items.remove(item)
                break

    @property
    def total_price(self) -> float:
        return sum(item.total_price for item in self.items)

    def __str__(self) -> str:
        return 'Cart items: ' + ''.join(f'\n\t{str(item)}' for item in self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Generator[Item]:
        return iter(self.items)


if __name__ == '__main__':
    cart = Cart()

    cart.add_item(Item('name1', 'url1', 1.00, 5))
    cart.add_item(Item('name2', 'url2', 5.00, 2))
    cart.add_item(Item('name3', 'url3', 10.00, 3))

    print(cart)
    print(cart.total_price)
    print(len(cart))

    cart.remove_item(Item('name2', None, None, None))

    item_list = []
    for item in cart:
        item_list.append(item)

    print(item_list)
