"""
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any 
letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a 
new string with the letters t, i, g, e, and r removed from it.

def tiggerfy(s):
	pass
Example Usage

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)
Example Output:

"suspcous"
""
"Hunny"
"""

def tiggerfy(s):
    #Remove the letters t, i, g, e, r
    st = ""
    tig = ['t', 'i', 'g', 'e', 'r']
    for i in s.lower(): 
        if i not in tig:
            st += i
    return st

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))
