class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linklist:
    def __init__(self):
        self.head=None
        
    def printll(self):
        if self.head is None:
            print('Linklist is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end="")
                n=n.next
                
    def addBegin(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
    def addEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=newNode
        
ll=Linklist()
ll.addBegin(10)
ll.addBegin(20)
ll.addEnd(40)
ll.printll()
