'''

Problem 3 - Printing Out all Available Letters
 Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, 
 lettersGuessed. This function returns a string that is comprised of lowercase English letters - 
 all lowercase English letters that are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz

Note that this function should return the letters in alphabetical order, as in the example above.
'''
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    myStr=list(string.ascii_lowercase)
    letters=''
    for i in lettersGuessed:
       if i in myStr:
          myStr.remove(i)
    for item in myStr:
       letters+=item
    return letters
