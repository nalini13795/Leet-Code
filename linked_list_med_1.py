'''

2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        fast = slow = head
        prev = head
        if(head.next):
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = slow.next
        else:
            head = None
            
        return head

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

result = Solution()
output = result.deleteMiddle(list1)
while(output):
    print(output.val)
    output = output.next