#trees
class Node:
    def __init__(self,root):
        self.left=None
        self.data=root
        self.right=None
class BST:
    def addnode(self,root,data):
        newdata=Node(data)
        if root==None:
            return newdata
        if data<root.data:
            if root.left!=None:
                self.addnode(root.left,data)
        else:
            if root.right!=None:
                self.addnode(root.right,data)
    def inorder(self,root):
        if root.left!=None:
            print(root.left.data,end=' ')
        
        print(root.data)
        if root.right!=None:
            print(root.right.data,end=' ')
    def preorder(self,root):
        print(root.data)
        if root.left!=None:
            print(root.left.data,end=' ')    
        if root.right!=None:
            print(root.right.data,end=' ')
    def postorder(self,root):
        if root.left!=None:
            print(root.left.data,end=' ')
        if root.right!=None:
            print(root.right.data,end=' ')
        print(root.data)
    def levelorder(self,root):
        q=[root]
        while len(q)!=0:
            ele=q.pop(0)
            print(ele.data,end=' ')
            if ele.left!=None:
                q.append(ele.left)
            if ele.right!=None:
                q.append(ele.right)
                
l=[16,9,25,4,10,8,83,15]
tree=BST()
root=None
root=tree.addnode(root,l[0])
print(root.data)
for i in range(1,len(l)):
    tree.addnode(root,l[i])

                
