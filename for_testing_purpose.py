def process_items(items: list[str]):
    for item in items:
        print(item.capitalize)

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")