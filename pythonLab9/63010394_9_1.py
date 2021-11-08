x = [int(i) for i in input('Enter Input : ').split()]
st = 0
m=[None]
v = 'None'
for j in range(len(x)-1):
        s = False
        for i in range(len(x)-j-1):
            if x[i]> x[i+1]:
                x[i],x[i+1] = x[i+1],x[i]
                s = True
                v = str(x[i+1])
                m.pop() 
                m.append(x.copy()) 
        if not s or j==len(x)-2:
            print(f'last step : {x} move[{v}]')
            isw = False
            break
        elif s:
            st+=1
            print(f'{st} step : {x} move[{v}]')
            v = 'None'

