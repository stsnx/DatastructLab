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
            print('*')
        else :
            intree = False
            temp = self.root
            while(not intree) :
                if temp.data<=data:
                    if temp.right==None:
                        temp.right = Node(data)
                        print('R*')
                        break
                    else :
                        print('R',end='')
                        temp = temp.right
                elif temp.data>data:
                    if temp.left==None:
                        temp.left = Node(data)
                        print('L*')
                        break
                    else :
                        print('L',end='')
                        temp = temp.left
        return self.root        
    def printtree(self, node, level = 0):
        if node != None:
            self.printtree(node.right, level + 1)
            print('     ' * level, node)
            self.printtree(node.left, level + 1)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    
