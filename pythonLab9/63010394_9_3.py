x = [int(i) for i in input('Enter Input : ').split()]
l =[]
r = []
l.append(x.pop(0))
for i in x:
    r.append(i)
n = len(r)
for i in range(n):
    t = r.pop(0)
    s = False
    for j in range(len(l)):
        if l[j]> t:
            l.insert(j,t)
            if len(r)>0:
                print(f'insert {t} at index {j} : {l} {r}')
            else :
                print(f'insert {t} at index {j} : {l}')
            s = True
            break
    if not s:
        l.insert(len(l),t)
        if len(r)>0:
            print(f'insert {t} at index {j+1} : {l} {r}')
        else :
            print(f'insert {t} at index {j+1} : {l}')
        s = False
print('sorted')
print(f'{l}')