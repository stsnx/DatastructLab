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

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
l = [x for x in s.split(',')]
if l[0]==str(0) : l=[]
S = Stack()
S.items = l
if o == 'arrive' :
    if S.size()== m:
        print("car "+str(n)+" cannot arrive : Soi Full")
    elif str(n) not in l :
        print("car "+str(n)+" arrive! : Add Car "+str(n))
        S.push(str(n))
    elif str(n) in l :
        print("car "+str(n)+" already in soi")
    
if o == 'depart' :
    if S.isEmpty():
        print("car "+str(n)+" cannot depart : Soi Empty")    
    elif str(n) not in l :
        print("car "+str(n)+" cannot depart : Dont Have Car "+str(n))
    elif str(n) in l :
        print("car "+str(n)+" depart ! : Car "+str(n)+" was remove")
        x=[]
        for i in S.items :
            if str(i)!=str(n):
                x.append(i)
        S.items = x
    

print(str(S.items).replace("\'",''))

