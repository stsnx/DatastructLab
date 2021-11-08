b = []
t = []
def check(x):
    if a[x] == 1 :
        t.append(int(a[x]))
        temp = t.copy()
        b.append(temp)
        n = t[0]
        t.clear()
        return n
    else :
        if x+1< len(a):
            if a[x]-1 == a[x+1]:
                t.append(int(a[x]))
                return check(x+1)
            else :
                t.append(int(a[x]))
                temp = t.copy()
                print(temp)
                n = temp[0]-temp[len(temp)-1]+1
                t.clear()
                return n
        else :
            return 1
print("*** Fun with countdown ***")
a = [int(i) for i in input("Enter List : ").split()]
c = 0
while(c<len(a)) :
    c+=check(c)
print(f'[{len(b)}, {b}]')