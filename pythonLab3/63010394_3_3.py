class Stack:
    def __init__(self,list = None) :
        if list== None :
            self.items = []
        else :
            self.items = list
    def push(self,i):
            self.items.append(i)
    def pop(self) :  
            return self.items.pop(len(self.items)-1)  
    def isEmpty(self) :
            return self.items==[]
    def size(self) :
            return len(self.items)

inp = input('Enter Input : ').split()

S = Stack()
x = ''
combo = 0
count = 0
for i in inp :
    S.push(i)
    if i == x :
        count+=1
    else :
        x=i
        count=1
    if count==3 :
        count=0
        S.pop()
        S.pop()
        S.pop()
        combo+=1
        if S.size()>1:
            if S.items[-2] == S.items[-1] :
                x=S.items[-1]
                count = 2
            else :
                x=S.items[-1]
                count = 1
        elif S.size()==1:
                x=S.items[-1]
                count = 1

print(S.size())
if S.size()==0: print('Empty',end='')
else :
    for i in range(S.size()-1,-1,-1):
        print(S.items[i],end='')
if combo>1 :
    print('\nCombo : '+str(combo)+' ! ! !')

