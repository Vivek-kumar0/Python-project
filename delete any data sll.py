class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Ll:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        if self.head is None:
            return True
            
    def addBegin(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
    def search(self,data):
        if self.head is not None:
            n=self.head
            while n is not None:
                if n.data==data:
                    print('present')
                
                n=n.next
            
        else:
            print('Empty')
        
       
            
            
    def dell(self,data):
        if self.head is None:
            pass
        elif(self.head.next is None):
            if self.head.data==data:
                self.head=self.head.next
        
        
        else:
            n=self.head
            while n.next is not None:
                if n.next.data==data:
                    n.next=n.next.next
                    break
                else:
                    if n.data==data:
                        self.head=self.head.next
                    
                    
                
                n=n.next

    def addAnyPosition(self,pos,data):
        newNode=Node(data)
        if pos==1:
            newNode.next=self.head
            #self.head.prev=newNode
            self.head=newNode
        else:
            n=self.head
            for i in range(pos-1):
                n=n.next
            newNode.next=n.next
            n.next=newNode
        
        
    def prntll(self):
        
        n=self.head
        while n is not None:
            print(n.data,'-->',end='')
            n=n.next
                
ll=Ll()
ll.addBegin(10)
ll.addBegin(5)
ll.addBegin(54)
ll.addBegin(89)
ll.addBegin(9)
ll.addAnyPosition(1,7)
ll.dell(89)
ll.prntll()
        
