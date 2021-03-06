#cAssume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur
# in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd',
# then your program should print
#Longest substring in alphabetical order is: abc

s = 'abcdcd'
maxLen = 0
current = s[0]
long = s[0]

for x in range(len(s) - 1):
    if s[x + 1] >= s[x]:
        current += s[x + 1]
        if len(current) > maxLen:
            maxLen = len(current)
            long = current
    else:
        current = s[x + 1]

    x += 1
print ('Longest substring in alphabetical order is: ' + long)
