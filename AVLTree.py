

class Node:
    def __init__(self,key=int,leftChild=None,rightChild=None,parent=None):
        self.key=key
        self.leftChild=leftChild
        self.rightChild=rightChild
        self.parent=parent
        self.balance=0
        
        
class AVLTree(Node):
    
    def __init__(self,key):
        Node.__init__(self,key)
        self.root=Node(key)
        self.balance=self.Height(self.root)
        
        
    def Update(self,node):
        curr=node
        while curr:
            curr.balance=self.Balance(curr)
            
            if curr.balance==2 and curr.rightChild.balance==-1:
                recht=curr.rightChild
                self.RightRotate(recht)
                self.LeftRotate(curr)
                break
                
            if curr.balance==-2 and curr.leftChild.balance in {0,-1}:
                self.RightRotate(curr)
                break
            
            if curr.balance==2 and curr.rightChild.balance in {0,1}:
                self.LeftRotate(curr)
                break
                
            if curr.balance==-2 and curr.leftChild.balance==1:
                link=curr.leftChild
                self.LeftRotate(link)
                self.RightRotate(curr)
                break
                
            curr.balance=self.Balance(curr)
            curr=curr.parent
    
    
    def Height(self,node): # hilf zu Berechnung von Tiefe des Baums
        if node==None:
            return -1
        if node.rightChild and node.leftChild:
            return 1+max(self.Height(node.leftChild),self.Height(node.rightChild))
        if node.leftChild:
            return 1+ self.Height(node.leftChild)
        if node.rightChild:
            return 1+ self.Height(node.rightChild)
        else:
            return 0
        
        
    def insert(self,key):
        z=Node(key)
        y=None
        x=self.root
        while x!=None:
            y=x
            if z.key<x.key:
                x=x.leftChild
            else:
                x=x.rightChild
        z.parent=y
        if y==None:
            self.root=z
        elif z.key<y.key:
            y.leftChild=z
        else:
            y.rightChild=z 
            
        self.root.balance=self.Balance(self.root) # hier wird die Balance von wirzel (root) berechnet
        self.Update(z) # hier soll man z updateten zo dass es zu einem AVL-baum wird
    
    
   
        
        
    def Balance(self,node): # Berechnung von Balance einer Node
        if node==None:
            return 0
        return self.Height(node.rightChild) - self.Height(node.leftChild)
    
    
    def RightRotate(self,x):
        y=x.leftChild
        if x.parent==None:
            self.root=y
        elif x.parent.leftChild==x:
            x.parent.leftChild=y
        else:
            x.parent.rightChild=y
        y.parent=x.parent
        x.leftChild=y.rightChild
        if x.leftChild!=None:
            x.leftChild.parent=x
        y.rightChild=x
        x.parent=y

        
    def LeftRotate(self,x):
        y=x.rightChild
        #print(x.parent)
        if x.parent==None:
            self.root=y
        #print(x.parent.leftChild)
        elif x.parent.leftChild==x:
            x.parent.leftChild=y
        else:
            x.parent.rightChild=y
        y.parent=x.parent
        x.rightChild=y.leftChild
        if x.rightChild!=None:
            x.rightChild.parent=x
        y.leftChild=x
        x.parent=y
