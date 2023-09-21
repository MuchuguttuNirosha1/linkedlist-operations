#Implementation of linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None 
#traversing a singly linked list
    def print_LL(self):
        if self.head is None:
            print("linked list is empty") 
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
LL1=Linkedlist()
LL1.print_LL()  
