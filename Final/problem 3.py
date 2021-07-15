'''
Write a function is_triangular that meets the specification below. 
A triangular number is a number obtained by the continued summation of integers starting from 1. 
For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers. 
'''

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    total=0
    while(k>=1):
        if k==1:
            return True
        else:
            for i in range(k):
                total+=i
                if total==k:
                    return True
            return False
