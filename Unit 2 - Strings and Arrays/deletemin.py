"""
Pooh is eating all of his hunny jars in order of smallest to largest. 
Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() that continuously 
removes the minimum element until the list is empty. Return a new list of the elements of hunny_jar_sizes
 in the order in which they were removed.

def delete_minimum_elements(hunny_jar_sizes):
	pass
Example Usage

hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)
Example Output:

[1, 2, 3, 4, 5]
[1, 2, 2, 5, 8]

"""

"""
understand: We will be removing the smallest in the list every time until we remove every number then we store it 
into a new list 

input: a array
output: a sorted array

constraints: none

edge case: Return a new list of the elements of hunny_jar sizes in the order they were removed

"""
def delete_minimum_elements(hunny_jar_sizes):
    arr = []
    while len(hunny_jar_sizes) > 0:
        minNum = min(hunny_jar_sizes)
        arr.append(minNum)
        hunny_jar_sizes.remove(minNum)
    return arr
				   


hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
			
        
      