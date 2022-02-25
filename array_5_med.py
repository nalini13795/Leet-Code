'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        arr = []
        neg = False
        max_int = 2147483648
        if(x<0):
            neg =True
            x *=-1
        while(x!=0):
            arr.append(x%10)
            x//=10
        for i in arr:
            rev = rev*10 + i
            if(rev >= max_int):
                return 0
        if(neg):
            return rev*-1
        else:
            return rev
        
            
        