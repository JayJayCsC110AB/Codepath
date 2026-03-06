"""
Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...

def print_todo_list(task):
	pass
Example Usage

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
Example Output:

Pooh's To Dos:
1. Count all the bees in the hive
2. Chase all the clouds from the sky
3. Think
4. Stoutness Exercises

Pooh's To Dos:

"""

def print_todo_list(task):
	print("pooh's to do list")
	for i in range(len(task)):
			print(f"{i+1}. {task[i]}")
			
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)
	

		
"""
    Understand: 
        I - Inputs
		tasks = array of inputs
        O - Outputs
		none
        C - Constraints
		none
        E - Edge cases and (examples)
            


    Plan: 
	
        key idea: we will use the task to loop through each array indices and number them 1 - n-1 
        as integers most likely we will be using multiple if statements
        Steps: 
        poohs to do
		i = 1
		for i in range(len(task))
            if i == task[i]
			  i, task[1]

Implement:
"""
