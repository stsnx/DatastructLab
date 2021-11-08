class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class Binarysearchtree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root==None:
            self.root = Node(val)
        else :
            intree = False
            temp = self.root
            while(not intree) :
                if temp.data<=val:
                    if temp.right==None:
                        temp.right = Node(val)
                        break
                    else :
                        temp = temp.right
                elif temp.data>val:
                    if temp.left==None:
                        temp.left = Node(val)
                        break
                    else :
                        temp = temp.left
        return self.root        
    def dele(self,r, data):
        if r == None :
            print('Error! Not Found DATA')
            return
        if r.data!=data:
            if r.data<=data:
                r.right = self.dele(r.right, data)
            elif r.data>data:
                r.left = self.dele(r.left, data)
        else:
            if r.right == None:
                r = r.left
                return r
            elif r.left == None:
                r = r.right
                return r
            else :
                temp = r.right
                while temp.left!=None :
                    temp = temp.left
                r.data = temp.data
                r.right = self.dele(r.right,temp.data)
                #print(str(f'{temp.left} {temp.data} {temp.right}'))
        return r       
def printtree90(node, level = 0):
    if node != None:
        printtree90(node.right, level + 1)
        print('     ' * level, node)
        printtree90(node.left, level + 1)

#i 8,i 7,d 1,i 3,i 1,i 2,i 6,i 9,d 8,d 9,d 7,d 1,d 6,d 3,d 2
tree = Binarysearchtree()
data = input("Enter Input : ").split(",")
for i in range (len(data)):
    t = data[i].split()
    if t[0]=='i':
        print('insert '+str(t[1]))
        tree.insert(int(t[1]))
        printtree90(tree.root)
    elif t[0]=='d':
        print('delete '+str(t[1]))
        tree.root = tree.dele(tree.root,int(t[1]))
        printtree90(tree.root)
#i 3,i 6,i 2,i 5,i 4,i 9,i 8,i 2,d 3
#i 3,i 2,i 1,i 12,i 7,i 17,i 5,i 11,i 13,i 19,i 4,i 6,i 9,i 15,d 18,i 20,i 8,i 10,i 14,i 16,d 12