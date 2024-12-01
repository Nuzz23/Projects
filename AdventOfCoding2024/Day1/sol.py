from collections import Counter

with open('./AdventOfCoding2024/Day1/data.txt', 'r', encoding='UTF-8') as fp:
    listA = []
    listB = []
    for line in fp:
        line = [int(item) for item in line.strip().split()]
        listA.append(line[0])
        listB.append(line[1])
    
    listA.sort()
    listB.sort()
        
    
print(sum(abs(listA[i]-listB[i]) for i in range(len(listA))))


conta = Counter(listB)
print(sum(number*conta[number]  for number in set(listA) if number))

