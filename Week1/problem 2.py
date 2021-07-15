# program that prints the number of times the string 'bob' occurs in s
#if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2 

bob=0
for i in range(len(s)):
    if 'bob' == s[i:i+3]:
        bob+=1
    i+=1
print("Number of times bob occurs is:",bob)
