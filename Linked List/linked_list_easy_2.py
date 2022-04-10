'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         printval = head
#         temp_val =[]
#         while printval is not None:
#             temp_val.append(printval.val)
#             printval = printval.next
            
#         temp = ListNode()
#         output = temp
#         for ele in temp_val[::-1]:
#             temp.next = ListNode(ele)
#             temp = temp.next
            
#         return(output.next)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while (curr):
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        

        return prev
            

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(9)

result = Solution()
output = result.reverseList(list1)
while output is not None:
    print(output.val)
    output = output.next
