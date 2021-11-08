class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class binarysearchtree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printtree90(node, level = 0):
    if node != None:
        printtree90(node.right, level + 1)
        print('     ' * level, node)
        printtree90(node.left, level + 1)

def father(r,data):
    if r.data ==data:
        print (f'None Because {data} is Root')
    if not data in data[0]:
        print ('Not Found Data')
    if r != None:
        if r.right!=None :
            if r.right.data==data:
                print(r.data)
                return 
            else :
                father(r.right, data)
        if r.left!=None :
            if r.left.data==data:
                print(r.data)
                return 
            else :
                father(r.left, data)

tree = binarysearchtree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printtree90(tree.root)
if data[1] not in data[0]:
        print ('Not Found Data')
else:
    father(tree.root,data[1])
#print(father(tree.root,data[1]))