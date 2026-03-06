"""
Given two lists lst1 and lst2, write a function exclusive_elemts() 
that returns a new list that contains the elements which are in lst1 but not in lst2 
and the elements that are in lst2 but not in lst1.

Example Usage

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)
Example Output:

["pooh", "roo", "eeyore", "owl"]
["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]
[]
"""
def exclusive_elemts(lst1, lst2):
    list3 = []

    for i in lst1:
        if i not in lst2:
            list3.append(i)

    for i in lst2:
        if i not in lst1:
            list3.append(i)

    return list3

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))