class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
l = []
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
    def closestValue(self,root,value):
        if root!=None :
            diff = abs(value - root.data)
            ans = 0
            l.append(root)
            while len(l)>0:
                temp = l[0]
                l.pop(0)
                if abs(value-temp.data)<diff:
                    diff = abs(value-temp.data)
                    ans = temp.data
                elif abs(value-temp.data)==diff:
                    if ans<temp.data:
                        ans = temp.data
                if temp.left != None:
                     l.append(temp.left)
                if temp.right != None:
                     l.append(temp.right)
        return ans
        
T = BST()
x,y = input('Enter Input : ').split('/')
diff = 0
inp = [int(i) for i in x.split()]
for i in inp:
    if abs(int(y)-i)<=abs(diff):
        diff = int(y)-i
    root = T.insert(i)
    T.printtree(T.root)
    print('--------------------------------------------------')
print(f'Closest value of {y} : {T.closestValue(T.root,int(y))}')
