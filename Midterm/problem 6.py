'''
Write a recursive procedure, called laceStringsRecur(s1, s2), which also laces together two strings. 
Your procedure should not use any explicit loop mechanism, such as a for or while loop. We have 
provided a template of the code; your job is to insert a single line of code in each of the 
indicated places.

For this problem, you must add exactly one line of code in each of the three places where we 
specify to write a line of code. If you add more lines, your code will not count as correct.
'''
def laceStringsRecur(s1, s2):
    '''
    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    :param s1: string
    :param s2: string
    :return: Interlaced strings
    '''
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            # If the first string is empty, append the second one to the output and STOP
            return out + s2
        if s2 == '':
            # If the first string is empty, append the second one to the output and STOP
            return out + s1
        else:
            # Append to the output the next character of each of the two strings
            # and recursively interlace the remaining sub-strings
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')
