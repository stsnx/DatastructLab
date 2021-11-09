l = [e for e in input("Enter Input : ").split()]
def sorandmed(x,fp,t):
    s = False
    for i in range(len(x)):
        if x[i]>t:
            x.insert(i,t)
            s = True
            break
    if not s:
        x.insert(len(x),t)
    if len(x)%2==0 and len(x)>0:
        z = (x[len(x)//2]+x[(len(x)//2)-1])/2
        print(f'list = {fp} : median = {z:.1f}')
    elif len(x)%2==1:
        z = x[len(x)//2]
        print(f'list = {fp} : median = {z:.1f}')
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    x = []
    fp = []
    for i in range(len(l)):
        t=l[i]
        fp.append(l[i])
        sorandmed(x,fp,t)