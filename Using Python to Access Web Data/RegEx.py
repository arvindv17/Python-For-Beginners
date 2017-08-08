import re

allNumbers = []

with open('regex_sum_14557.txt') as f:
    text = f.read().splitlines()


for line in text:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        allNumbers.append(int(number))

print (sum(allNumbers))