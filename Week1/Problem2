# Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print Number of times bob occurs is: 2
#
#Methode 1:
s = 'azcbobobbobegghakl'
count = 0
for x in range(len(s)) :
    if s[x:x+3] == 'bob' :
        count += 1
print('Number of times bob occurs is: ' + str(count))

#Methode 2:
s = 'azcbobobbobegghakl'
count = 0
x = 0
y = 1
z = 2
while z < len(s):
    if s[x] == 'b' and s[y] == 'o' and s[z] == 'b':
        count += 1
    x += 1
    y += 1
    z += 1
print("Number of times bob occurs is:" + str(count))

# My own example to better understending of subject:

s = "tomatoeggtomatoeggbacontomatojuicebecontomato"
count = 0
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
while f < len(s):
    if s[a] == 't' and s[b] == 'o' and s[c] == "m" and s[d] == 'a' and s[e] == 't' and s[f] == 'o':
        count += 1
    a += 1
    b += 1
    c += 1
    d += 1
    e += 1
    f += 1
print("Number of times tomato occurs is:" + str(count))

s = 'tomatoeggtomatoeggbacontomatojuicebecontomato'
count = 0
a = 5
for x in range(len(s)):
    if s[x:x+5] == 'tomato':
        count += 1
print('Number of times tomato occurs is:' + str(count))
