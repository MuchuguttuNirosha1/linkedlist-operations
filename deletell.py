#deletion from beginnning,middle and end of the singly linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("linked list is empty") 
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we cant delete nodes")
        else:
            self.head=self.head.ref
    def delete_by_value(self,x):
        if self.head is None:
            print("can't delete LL is empty")
            return 
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("node is not present")
        else:
            n.ref=n.ref.ref
    def delete_end(self):
        if self.head is None:
            print("LL is empty so we cant delete nodes")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
            
            
LL1=LinkedList()
LL1.add_begin(10)
LL1.add_end(20)
LL1.add_after(30,10)
LL1.delete_begin()
LL1.delete_end()
LL1.delete_by_value(30)
LL1.print_LL()
