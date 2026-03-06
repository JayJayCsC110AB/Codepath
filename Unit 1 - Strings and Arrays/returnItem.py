items = ["piglet", "pooh", "roo", "rabbit"]

def get_items(items, x):
    if 0 <= x < len(items):
        print(f"{items[x]}, {x}")
    else:
        print("None")

x = 0
get_items(items, x)