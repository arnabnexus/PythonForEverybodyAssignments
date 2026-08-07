import re

name = input("Enter file:")
if len(name) < 1:
    #name = "regex_sum_42.txt"
    name = "regex_sum_2454922.txt"
"""
handle = open(name)

total = 0

for line in handle:
    line = line.rstrip()   
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        total += int(number)
print(total)
"""
#Alternate Single line code
#List Comprehension
print(sum([int(number) for number in re.findall('[0-9]+',open(name).read()) ] ) )