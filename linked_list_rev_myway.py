

class Node():
    def __init__(self, val =0) -> None:
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.headval = None
    
    def create_linked_list(self,val):
        new_node = Node(val)
        link_list = self.headval
        while (link_list.next):
            link_list = link_list.next
        
        link_list.next = new_node

    def print_linked_list(self):
        printval = self.headval
        while printval:
            print(printval.val)
            printval = printval.next
    
    def rev_list(self):
        curr = self.headval
        prev = None
        while(curr):
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        while(prev):
            print(prev.val)
            prev = prev.next

if __name__ == "__main__":
    llist = LinkedList()
    llist.headval = Node(1)
    llist.create_linked_list(2)
    llist.create_linked_list(3)
    llist.create_linked_list(4)
    llist.create_linked_list(5)
    llist.rev_list()
    # llist.print_linked_list()


