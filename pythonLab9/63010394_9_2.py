x = [int(i) for i in input('Enter Input : ').split()]
Ma = 0
temp = 0
for i in range(len(x)-1,0,-1):
    for j in range(i):
        if x[j] > Ma :
            Ma = x[j]
            temp = j
    if Ma > x[i]:
        x[temp],x[i] = x[i],Ma 
        print(f'swap {x[temp]} <-> {x[i]} : {x}')
    Ma=0
print(x)
