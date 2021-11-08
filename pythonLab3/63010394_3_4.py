class Stack :

    def __init__(self,list = None) :
        if list== None :
            self.items = []
        else :
            self.items = list

    def isEmpty(self) :
        return self.items==[]
    def push(self,data) :
        self.items.append(data)
    def pop(self) :
        return self.items.pop(len(self.items)-1)  
    def size(self) :
        return len(self.items)
    def peek(self) :
        return self.items[len(self.items)-1]
oper = Stack()
v = Stack()
ans = []
def infix2postfix(token):
    t = "+-*/()"
    r1 = "()"
    r2 = "*/"
    r3 = "+-"
    for i in token:
        if i in t:
            if oper.isEmpty():
                oper.push(i)
            else :
                if i in r2:
                    #ans.append(i)
                    while oper.peek() in r2:
                        ans.append(oper.peek())
                        oper.pop()
                        if oper.isEmpty() : break
                    oper.push(i)
                elif i in r3:
                    #ans.append(i)
                    while oper.peek() in r2 or oper.peek() in r3:
                        ans.append(oper.peek())
                        oper.pop()
                        if oper.isEmpty() : break
                    oper.push(i)
                elif i ==')':
                    while oper.peek() != '(': 
                        ans.append(oper.peek()) 
                        oper.pop()
                        if oper.isEmpty() : break
                else :
                    oper.push(i)
        else :
             ans.append(i)
    while not oper.isEmpty():
        i = oper.peek()
        if i!='(':
         ans.append(i)
        oper.pop()
    return str(ans).replace(',','').replace('[','').replace(']','').replace(' ','').replace('\'','')
print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))