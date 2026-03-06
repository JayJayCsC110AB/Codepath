"""
Winnie the Pooh and his friends are playing a game called Poohsticks 
    where they drop sticks in a stream and race them. 
    They time how long it takes each player's stick to float under Poohsticks Bridge to score
     each round.

Write a function count_less_than() to help Pooh and his friends determine how many 
    players should move on to the next round of Poohsticks. 
    count_less_than() should accept a list of integers race_times and an integer threshold 
        and return the number of race times less than threshold

input: race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

output = 3

input: race_times = []
threshold = 4
count_less_than(race_times, threshold)

output = 0
"""
def count_lessthan(race_times, threshold):
 number = 0
 for i in range(len(race_times)):
  if race_times[i] <= threshold:
    number +=1
 return number
 
 """
    Understand: 
        I - Inputs
         race_times = an array of seconds in the race times
         threshold = an integer of seconds
        O - Outputs
            return x = number of race times less than threshold
         
        C - Constraints
            none
        E - Edge cases and (examples)
            


    Plan: 
        key idea: To iterate through the array 
        and check how many variables are less than the seconds 
        of the threshold
        Steps: 
            x = 0
            for i in range(race_times)
                if i >= 0
                    add 1 to x
            return x once loop ends

Implement:
"""


race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_lessthan(race_times, threshold))


race_times = []
threshold = 4
print(count_lessthan(race_times, threshold))