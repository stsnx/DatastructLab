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
m,n = input("Enter Input : ").split('/')
mem =[]
line = Queue()
l = [i for i in m.split(',')]
o = [i for i in n.split(',')]
max =0
for i in l:
    t = i.split()
    x = int(t[0])
    if x>max : max =x
for i in range(max+1):
    mem.append(Queue())
for i in l:
    t = i.split(' ')
    mem[int(t[0])].push(t[1])
for i in o:
    t = i.split(' ')
    if t[0] == 'D' :
        if line.isEmpty():
            print("Empty")
        else :
            x = line.front().split(" ")
            print(x[0])
            line.pop()
    if t[0] == 'E' :
        data = t[1]
        templine= []
        found = 0
        pn =0
        for j in range(len(mem)):
            if data in mem[j].items:
                data+=' '+str(j)
                pn = j
        if len(line.items)>1:
            templine = []   
            for j in range(len(line.items)-1) :
                x = line.items[j].split()
                xn = line.items[j+1].split()
                if pn == int(x[1]) and pn != int(xn[1]):
                    templine.append(line.items[j])
                    templine.append(data)
                    found=1
                else :
                    templine.append(line.items[j])
            templine.append(line.items[len(line.items)-1])
            if found ==0:
                templine.append(data)
        else :
            templine = line.items.copy()
            templine.append(data)
        line.items = templine.copy()


        








        

