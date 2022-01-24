'''
My stupid solution
Product of Array Except Self
'''

# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         product = 1
#         index_0 = 0
#         result = []
#         for i in nums:
#             if(i!=0):
#                 product *= i
#         indices = [index for index, element in enumerate(nums) if element == 0]
#         if(len(indices)>=2):
#             return [0 for i in nums]
#         elif(len(indices)==1):
#             for i in range(len(nums)):
#                 if(i==indices[0]):
#                     result.append(product)
#                 else:
#                     result.append(0)
#             return result
#         else:
#             return [product/i for i in nums]
'''
computing the left product nad then computing the right product... then multipying both the products
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        L[0] = 1
        for i in range(1,length):
            L[i] = L[i-1]*nums[i-1]
        
        R[-1] = 1
        for i in reversed(range(length-1)):
            R[i] = R[i+1]*nums[i+1]
            
        for i in range(length):
            answer[i] = L[i]*R[i]
            
        return answer
        

result = Solution()
print(result.productExceptSelf([1,2,3,4]))