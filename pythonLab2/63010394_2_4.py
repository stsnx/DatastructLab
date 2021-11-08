def findzero(y):
    ans = []
    for i in range(0,len(y)):
        for k in range(i+1,len(y)):
            for j in range(k+1,len(y)):
                if y[i]+y[j]+y[k] == 0 :
                    temp = [y[i],y[k],y[j]]
                    if temp not in ans :
                        ans.append(temp)
    print(ans)
x=[int(i) for i in input("Enter Your List : ").split(' ')]
print("Array Input Length Must More Than 2") if len(x)<3 else findzero(x)