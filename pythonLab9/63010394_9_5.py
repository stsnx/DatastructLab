x,y = input('Enter Input : ').split('/')
def s(x):
    for i in range(len(x)):
        for j in range(i,len(x)):
          if x[i]>x[j]:
              y = x[j]
              x[i],x[j] = y,x[i]
    return x
def findsum(data,v,l=0,res=[],temp=[]) :
    if l>=len(data):
     return res
    else :
        temp.append(data[l])
        if sum(temp) == v:
            res.append(temp.copy())
        res = findsum(data,v,l+1,res,temp)
        temp.pop()
        res = findsum(data,v,l+1,res,temp)
    return res
def sao(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if len(a[i])>len(a[j]):
                y = a[j]
                a[i],a[j] = y,a[i]
            elif len(a[i])==len(a[j]):
                ta,tb=a[i],a[j]
                tx,ty=ta[0],tb[0]
                for k in range(len(ta)):
                    if tx!=ty:
                        break
                    else :
                        tx,ty=ta[k],tb[k]
                if tx>ty:
                    y = a[j]
                    a[i],a[j] = y,a[i] 
    return a
z = [int(i) for i in y.split()]
zz = s(z)
ans = findsum(z,int(x))
sa = sao(ans)
if len(sa)==0:
    print('No Subset')
else :
    for i in sa:
        print(i)
