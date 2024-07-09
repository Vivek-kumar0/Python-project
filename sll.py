class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Sll:
    def __init__(self):
        self.head=None
        
    def addBegin(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
    def addEnd(self,data):
        newNode=Node(data)
        if self.head is not None:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=newNode
            
        else:
            self.head=newNode
            
    
    def printll(self):
        if self.head is None:
            print('Sll is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end='')
                n=n.next
                
    def addAnyPosition(self,pos,data):
        newNode=Node(data)
        if pos==1:
            newNode.next=self.head
            self.head=newNode
        else:
            n=self.head
            for i in range(1,pos-1):
                n=n.next
            
            newNode.next=n.next
            n.next=newNode
            
    def removeAnyPosition(self,pos):
        if pos==1:
            self.head=self.head.next
        else:
            n=self.head
            a=n.next
            for i in range(1,pos-1):
                a=a.next
                n=n.next
            
            n.next=a.next
            a.next=None
s=Sll()
s.addEnd(2)
s.addBegin(5)
s.addBegin(15)
s.addEnd(1)
s.addAnyPosition(5,4)
s.removeAnyPosition(3)
s.printll()
                
    
