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

x = [i for i in input("Enter Input : ").split(',')]
q = Queue()
for i in x :
    t = i.split(' ')
    if t[0] == "E":
        q.push(t[1])
        print(q.size())
    elif t[0] == "D":
        if q.isEmpty() :
         print("-1")
        else :
            print(f'{q.front()} 0')
            q.pop()
if q.isEmpty() :
    print("Empty")
else :
    print(str(q.items).replace("[",'').replace("]",'').replace("\'",'').replace(",",''))