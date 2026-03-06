def can_pair(quantity):
    list = []
    for digits in range(1, quantity+1):
        if quantity % digits == 0:
            list.append(digits)
    return list

quantity = 6
print(can_pair(quantity))