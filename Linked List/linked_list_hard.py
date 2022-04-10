'''
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''
# Naive approch
# Traverse all the linked lists and collect the values of the nodes into an array.
# Sort and iterate over this array to get the proper value of nodes.
# Create a new sorted linked list and extend it with the new nodes.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        output = ListNode(-1)
        result = output
        n = len(lists) 
        temp = []
        for i in range(n):
            head = lists[i]
            while(head):
                temp.append(head.val)
                head = head.next
        
        for i in sorted(temp):
            output.next = ListNode(i)
            output = output.next
        return result.next
            
'''

Almost the same as the one above but optimize the comparison process by priority queue. You can refer here for more information about it.
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

'''