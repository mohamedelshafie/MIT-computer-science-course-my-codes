'''
Write a Python function called satisfiesF that has the specification below. 
Then make the function call run_satisfiesF(L, satisfiesF)
For your own testing of satisfiesF, for example, see the following test function f and test code:

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)

Should print:

2
['a', 'a']

Paste your entire function satisfiesF, including the definition, in the box below. 
After you define your function, make a function call to run_satisfiesF(L, satisfiesF). 
Do not define f or run_satisfiesF. Do not leave any debugging print statements.
'''
# Paste your function here
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here

    # Create a copy of L to iterate over
    newList = L[:]

    # Iterate over the copy of the list newList, make any changes to L
    for i in newList:
        if f(i)==False:
            L.remove(i)
    # Debug statement, comment out before submitting
    # print L
    return len(L)

# Calling run_satisfiesF(), leave in when submitting
run_satisfiesF(L, satisfiesF)