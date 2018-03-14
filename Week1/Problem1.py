# PROBLEM 1 from MiTx6.00.1x:
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
# your program should print: Number of vowels:
# There is str before count in last line becouse we want to change int to str that can fit there.
# count = 0 becouse we start counting from zero and adding 1 for letter what we intrest in.

#PROBLEM1:
#Variables for problem 1
s = 'aaeiuoliujfdsaasdfoeiu'
count = 0
for letter in s:
    if letter in 'aeiou':
        count += 1
print ('Number of vowels: ' + str(count))


# My own exampel to better understending of subject:
# a = exemplary string
# count = 0 becouse we start counting from zero and adding 1 for letter what we intrest in.

#EXAMPLE:
#Variables for example
a = 'Egg'
count = 0
for letter in a:
    if letter in 'g':
        count += 1
print('In Egg there is: ' + str(count) + ' "G" letters')
