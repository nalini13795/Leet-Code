'''
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list_result = ListNode()
        temp = list_result
        
        while (list1 is not None and list2 is not None):
            if(list1.val >= list2.val):
                list_result.next = ListNode(list2.val)
                list_result = list_result.next
                list2 = list2.next
            elif(list1.val < list2.val):
                list_result.next = ListNode(list1.val)
                list_result = list_result.next
                list1 = list1.next
                
            
        if(list1 is not None):
            list_result.next = list1
        else:
            list_result.next = list2
            
        return(temp.next)

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(2)
list2 = ListNode(9)
list2.next = ListNode(10)

result = Solution()
output = result.mergeTwoLists(list1,list2)
while output is not None:
    print(output.val)
    output = output.next