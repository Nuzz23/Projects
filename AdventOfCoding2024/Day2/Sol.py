with open('./AdventOfCoding2024/Day2/data.txt', 'r', encoding='UTF-8') as fp:
    data = [list(map(lambda x: int(x), line.strip().split())) for line in fp]
    
    
sol = [1]*len(data)
for j in range(len(data)):
    ascending = data[j][0] < data[j][1]
    for i in range(len(data[j])-1):
        if (not ( 1<= abs(data[j][i+1]-data[j][i]) <=3 )) or ((data[j][i] > data[j][i+1]) if ascending else (data[j][i]<data[j][i+1])):
            sol[j] = 0

        
print(sum(sol))


sol = [1]*len(data)
for j in range(len(data)):
    ascending = data[j][0] < data[j][1]
    #ascending = (data[j][0] < data[j][1] and data[j][1] < data[j][2]) or  (data[j][1] < data[j][2] and data[j][2] < data[j][3])
    for i in range(len(data[j])-1):
        if (not ( 1<= abs(data[j][i+1]-data[j][i]) <=3 )) or ((data[j][i] > data[j][i+1]) if ascending else (data[j][i]<data[j][i+1])):
            if sol[j] == -1:
                sol[j] = 0 
                break
            else:
                sol[j] = -1
                
    if sol[j] == -1:
        sol[j] = 1


        
print(sum(sol))