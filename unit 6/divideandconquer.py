"""
    It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order, use binary search to return True if there is a cruise length that matches vacation_length and False otherwise.

def find_cruise_length(cruise_lengths, vacation_length):
    pass
Example Usage:

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
Example Output:

True
False
    
    """
    
"""
    
  # Understand 
    inputs: array sorted list of integers representing the cruise length, and integer target representing vacation length
    outputs: boolean: if the integer in array of integers is seen, true if target exist, or false otherwise
    constraints: list must be sorted, and use binary search, 
    edge cases: if list is empty
    check true or false
    if its a single element
    
    

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
   binary search: so we will use two pointers left, right, and middle = left + right//2

  # Plan (pseudocode) 
  initiliaze left, right = 0, lenght of list - 1
  loop through using while loop while list is less than or equal right
  create search mid = (left + right)//2
  check if left <= right
   left = mid + 1
   if left >= right:
   left = mid - 1
   else: 
        return false
return true
    
  
  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
        
    
    
    """
def find_cruise_length(cruise_lengths, vacation_length):
    left, right = 0, len(cruise_lengths)-1
    
    while (left <= right):
        mid = (left + right)//2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            right = mid -1
    return False
            
        
print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

    