"""
Problem Set Version 1
Problem 1: Reverse Sentence
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed.
 The sentence will contain only alphabetic characters and spaces to separate the words. 
 If there is only one word in the sentence, the function should return the original string.

def reverse_sentence(sentence):
    pass
Example Usage:

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)
Example Output:

"fluff with stuffed all cubby little tubby"
"Pooh"

"""

"""
 We have a string with a sentence. The goal is to flip the String but not the characters of the string. 

    our inputs are: A string of words
    our output is: a returned reverse string
    constraints: none
    edge case: the function should return the orignal string if no spaces

"""

#plan we iterate through the string first 
def reverse_sentence(sentence):
    #initiate a str: that will hold the values of the str
    revstr = ""
    character = sentence.split()
    #reverse the str : start stop increment
    for i in range(len(character)-1, -1, -1):
        revstr += character[i] + " "
    return revstr.strip()


sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))