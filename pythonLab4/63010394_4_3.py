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
def encodemsg(x, y):
    e = Queue()
    t = x
    tn = y
    bn = y.items.copy()
    while not t.isEmpty():
        n = tn.front()
        text = ord(t.front())+int(n)
        if ord(t.front())>64 and ord(t.front())<91:
            if text > 90 :
                text = 64+(text-90)
            e.push(chr(text))
        if ord(t.front())>96 and ord(t.front())<123:
            if text > 122 :
                text = 96+(text-122)
            e.push(chr(text))
        t.pop()
        tn.push(tn.front())
        tn.pop()
    t.items = e.items.copy()
    y.items = bn.copy()
    print("Encode message is :  "+str(e.items))
def decodemsg(x, y):
    e = Queue()
    t = x
    tn = y
    bn = y.items.copy()
    while not t.isEmpty():
        n = tn.front()
        text = ord(t.front())-int(n)
        if ord(t.front())>64 and ord(t.front())<91:
            if text <65 :
                text = 91-(65-text)
            e.push(chr(text))
        if ord(t.front())>96 and ord(t.front())<123:
            if text <97 :
                text = 123-(97-text)
            e.push(chr(text))
        t.pop()
        tn.push(tn.front())
        tn.pop()
    t.items = e.items.copy()
    y.items = bn.copy()
    print("Decode message is :  "+str(e.items))
x = input("Enter String and Code : ").split(',')
s = str(x[0]).replace(' ','')
q1 = Queue()
q2 = Queue()
for i in s:
    q1.push(i)
for i in x[1]:
    q2.push(i)
encodemsg(q1,q2)
decodemsg(q1,q2)