"""
Write a function nanana_batman() 
that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. 
Do not use the * operator.

input: x = 6
output: "nananananana batman!

input: x=0
output: "batman!"
"""

def nanana_batman(x):
    """
    Understand: 
        I - Inputs
            x: ints the number of times we should print "na"
        O - Outputs
            none
        C - Constraints
            Do not use the * operator
        E - Edge cases and (examples)
            x<0:
            x = 0:
            x>0:


    Plan: 
        key idea: initialize a prefix variable and add to it a "na" of x times. 
        Then append to batman and print the string

        Steps: 
            x < 0:
                return 
            x = 0: 
                print("batman!)
            x > 0:

            initialize prefix to var to an empty string
            for i in range(x)
                add "na" to prefix
            add prefix to "batman!"
        print the entire prefix

    Implement:
    """

    if x < 0:
        return
    elif x == 0:
        print("batman!")
    else:
        prefix = ""
        for i in range(x):
            prefix += "na"
        print(prefix + " batman!")

nanana_batman(0)
nanana_batman(5)