def sor(i,j,t):
    if j<=len(t)-1:
        if t[i]<t[j]:
            x = t[i]
            t[i] = t[j]
            t[j] = x
        sor(i,j+1,t)
    if j==len(t) and i!=len(t)-1:
        sor(i+1,i+2,t)
#-3,-2,-1t = input('Enter your List : ').split(',')
d = [int(i) for i in input('Enter your List : ').split(',')]
sor(0,1,d)
print("List after Sorted : "+str(d).replace('\'',''))