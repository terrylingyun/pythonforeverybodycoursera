file = open('regex_sum_374256.txt')
numbers = list()
total = 0
import re
for line in file :
    numbers = numbers + re.findall('[0-9]+', line)
for number in numbers :
    number = int(number)
    total = total + number
print(total)
