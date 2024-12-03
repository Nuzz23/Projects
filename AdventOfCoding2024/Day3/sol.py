import re

with open('./AdventOfCoding2024/Day3/data.txt', 'r', encoding='UTF-8') as fp:
    string = ''.join([item.strip() for item in fp])
    

somma = 0
for item in re.findall("mul\([0-9]+,[0-9]+\)", string):
    item = item[4:-1].split(',')
    somma += int(item[0])*int(item[1])

print(somma)

somma = 0
for item in string.split('do()'):
    item = item.split('don\'t()')[0]
    for i in re.findall("mul\([0-9]+,[0-9]+\)", item):
        i = i[4:-1].split(',')
        somma += int(i[0])*int(i[1])

print(somma)




