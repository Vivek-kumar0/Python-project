class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkList:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("linkList is empty")

        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.ref

    def add_begin(self,data):
        new_node =node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node =node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                
                
                n=n.ref

            n.ref = new_node

lin=linkList()
lin.add_begin(10)
lin.add_end(100)
lin.add_end(500)
lin.add_begin(20)
lin.print_ll()
                
