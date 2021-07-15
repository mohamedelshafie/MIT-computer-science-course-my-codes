# program that counts up the number of vowels contained in the string s
vowels=0
for x in s:
    if x=='a' or x=='e'or x=='i' or x=='o' or x=='u':
        vowels = vowels + 1
print("Number of vowels: ",vowels)