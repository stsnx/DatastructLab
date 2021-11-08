class DoublyLinkedList : #Circular Doubly linked list with dummy
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.dummy = self.Node(None,None,None)
            self.dummy.next = self.dummy.prev = self.dummy
            self.size = 0
            
    def __str__(self):
        s = ''
        p = self.dummy.next
        for i in range(len(self)-1) :
            s += str(p.data) + ' '
            p = p.next
        s += str(p.data)
        return s  

    def __len__(self) :
        return self.size
        
    def isEmpty(self) :
        return self.size == 0
    
    def indexOf(self,data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p
    def str_reverse(self):
        s = ''
        p = self.nodeAt(len(self)-1)
        for i in range(len(self)-1) :
            s += str(p.data) + ' '
            p = p.prev
        s += str(p.data)
        return s 
    def add_before(self,q,data) :
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1
        
    def append(self,data) :
        self.add_before(self.nodeAt(len(self)),data)
  
    def removeNode(self,q) :   
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1
     
        
    def delete(self,i) :
        self.removeNode(self.nodeAt(i))
cur = 0
ll = DoublyLinkedList()
li = input('Enter Input : ').split(',')
ll.append('|')
for i in li:
    t= i.split(' ')
    if t[0] =='I':
        ll.add_before(ll.nodeAt(cur),t[1])
        cur+=1
    elif t[0] =='L':
        if cur>0:
            ll.add_before(ll.nodeAt(cur-1),'|')
            ll.delete(cur+1)
            cur-=1
    elif t[0] =='R':
        if cur<len(ll)-1 and cur>=0:
            ll.add_before(ll.nodeAt(cur+2),'|')
            ll.delete(cur)
            cur+=1
    elif t[0] =='B':
        if cur>0:
            ll.delete(cur-1)
            cur-=1
    elif t[0] =='D':
        if cur<len(ll)-1 and cur>=0:
            ll.delete(cur+1)
print(ll)


