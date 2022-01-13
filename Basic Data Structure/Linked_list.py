
'''
Singly linked List with
1. Print Linked list
2. Add in the begining
3. Add in the end
4. delete at start
5. delete at end
6. delete by value

'''

class Node():
    def __init__(self, val=None):
        self.val = val
        self.nextval = None

class LinkedList():
    def __init__(self):
        self.headval = None

    def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.val)
         printval = printval.nextval
    
    def add_at_end(self,val):
        new_node = Node(val)
        if self.headval is None:
            self.headval = new_node
            return
        else:
            list = self.headval
            while (list.nextval):
                list = list.nextval                                     
            list.nextval = new_node
    
    def add_at_start(self,val):
        new_node = Node(val)
        new_node.nextval = self.headval
        self.headval = new_node

    def delete_last(self):
        list = self.headval
        while(list.nextval.nextval):
            list = list.nextval
        list.nextval = None

    def delete_first(self):
        list = self.headval
        self.headval = list.nextval

    def delete_elem(self,val):
        list = self.headval
        if(self.headval.val == val):
            self.delete_first()
        else:
            while(list.nextval):
                if(list.val == val):
                    prev.nextval = list.nextval
                prev = list
                list = list.nextval


list = LinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
list.add_at_end("Thurs")
list.add_at_start("Sun")
# list.listprint()
# print("after delete last")
# list.delete_last()
# list.listprint()
# print("after delete first")
# list.delete_first()
list.listprint()
list.delete_elem("Wed")
list.listprint()

