def can_pair(item_quantities):
    for digits in item_quantities:
        if digits % 2 != 0:
            return False
    return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 2, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))