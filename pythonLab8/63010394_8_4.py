class Node:
    def __init__(self, data,power):
        self.data = data
        self.power = power
    
    def __str__(self):
        return str(self.data)+' '+str(self.power)
class FBST:

    def __init__(self):
        self.l=[]
    def insert(self,data,power):
        self.l.append(Node(data,power))
    def left(self,temp):
        if (temp.data*2)+1<len(self.l):
            return self.l[(temp.data*2)+1]
        else :
            return None
    def right(self,temp):
        if (temp.data*2)+2<len(self.l):
            return self.l[(temp.data*2)+2]  
        else :
            return None  
def findsum(node,x):
    li = []
    s =0
    temp = node.l[x]
    li.append(temp)
    while len(li)>0:
        tempo = li[0]
        li.pop(0)
        if node.left(tempo)!=None:
            li.append(node.left(tempo))
        s+=tempo.power
        if node.right(tempo)!=None:
            li.append(node.right(tempo))
    return s
def keqingDaBest(node,a,b):
    sa = findsum(node,a)
    sb = findsum(node,b)
    if sa<sb:
        return str(a)+'<'+str(b)
    elif sa>sb:
        return str(a)+'>'+str(b)
    elif sa==sb:
        return str(a)+'='+str(b)
T = FBST()
x,y = input('Enter Input : ').split('/')
com = [i for i in y.split(',')]
inp = [int(i) for i in x.split()]
for i in range(len(inp)):
    root = T.insert(i,inp[i])
print(str(findsum(T,0)))
for i in com :
    temp = [j for j in i.split()]
    print(keqingDaBest(T,int(temp[0]),int(temp[1])))
    


