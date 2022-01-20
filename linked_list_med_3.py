'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

'''
# My solution
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp ={}
        flag = 1
        copy_ll = head
        while(head):
            temp[flag]= head
            flag+=1
            head = head.next
            
        els = list(temp.items())
        to_remove = els[-n]
        
        prev = None
        curr = copy_ll
        
        if(curr.next == None and n==1):
            return None
        else:    
            while curr:
                if(curr == to_remove[1]):
                    if(prev):
                        prev.next = curr.next
                    else:
                        copy_ll = copy_ll.next
                    break
                else:
                    prev = curr
                    curr = curr.next

            return copy_ll

# optimized solution

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy
        
        for i in range(1,n+1):
            first = first.next
            
        while(first.next):
            second = second.next
            first = first.next
        
        second.next = second.next.next
        return dummy.next
            
            