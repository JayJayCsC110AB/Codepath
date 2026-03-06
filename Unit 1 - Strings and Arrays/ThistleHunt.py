"""Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles()
 that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". 
 The indices in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
	pass
Example Usage

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)
Example Output:

[0, 3]
[]

"""
#similiar to last program however this time we will be returning a list of indicies
# most likely we will be appending to a new array after looping through items 
# we will use a if statement to compare 

def locate_thistles(items):
	isThistle = []
	check = "thistle"
	for i in range(len(items)):
		if items[i] == check:
			isThistle.append(i)
	return isThistle

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))
            
	
