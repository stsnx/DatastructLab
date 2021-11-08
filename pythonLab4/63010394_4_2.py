class Queue:
    def __init__(self,list = None) :
        if list== None :
            self.items = []
        else :
            self.items = list
    def push(self,i):
            self.items.append(i)
    def pop(self) :  
            return self.items.pop(0)  
    def isEmpty(self) :
            return self.items==[]
    def size(self) :
            return len(self.items)
    def front(self) :
            return self.items[0]  
Q = Queue()
q1  = Queue()
q2  = Queue()
s = input("Enter people : ")
for i in s : 
    Q.push(i)
m = 0
m1 =0
m2=0
while(1):
    m+=1
    if q1.size()<5:
        q1.push(Q.front())
        Q.pop()
    else :
        q2.push(Q.front())
        Q.pop()
    print(f'{str(m)} {Q.items} {q1.items} {q2.items}')
    if not q1.isEmpty():
        m1+=1
    if not q2.isEmpty():
        m2+=1  
    if m1==3 :
        q1.pop()
        m1=0
    if m2==2 :
        q2.pop()
        m2=0
    if Q.isEmpty() :
        break