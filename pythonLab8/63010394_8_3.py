class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class BST:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root==None:
            self.root = Node(data)
        else :
            intree = False
            temp = self.root
            while(not intree) :
                if temp.data<=data:
                    if temp.right==None:
                        temp.right = Node(data)
                        break
                    else :
                        temp = temp.right
                elif temp.data>data:
                    if temp.left==None:
                        temp.left = Node(data)
                        break
                    else :
                        temp = temp.left
        return self.root        
    def printtree(self, node, level = 0):
        if node != None:
            self.printtree(node.right, level + 1)
            print('     ' * level, node)
            self.printtree(node.left, level + 1)
rank = 0
def inorder(t):
    global y
    global rank
    temp = t
    if temp.left!=None:
        inorder(temp.left)
    if t.data <= int(y):
        rank+=1
    if temp.right!=None:
        inorder(temp.right)
T = BST()
x,y = input('Enter Input : ').split('/')
inp = [int(i) for i in x.split()]
for i in inp:
    root = T.insert(i)
inorder(T.root)
T.printtree(T.root)
print('--------------------------------------------------')
print(f'Rank of {y} : {rank}')
