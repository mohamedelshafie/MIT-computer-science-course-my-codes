# program that prints the longest substring of s in which the letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print

#Longest substring in alphabetical order is: beggh

#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print ('Longest substring in alphabetical order is:', longest)