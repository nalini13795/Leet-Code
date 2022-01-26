'''
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        for ele in s:
            if(ele=='(' or ele == '[' or ele == '{'):
                arr.append(ele)
            elif(len(arr)>0):
                if(ele == ')'):
                    if(arr.pop() != '('):
                        return False
                elif(ele == ']'):
                    if(arr.pop() != '['):
                        return False
                elif(ele == '}'):
                    if(arr.pop() != '{'):
                        return False
            else:
                return False
        if(len(arr)!=0):
            return False
        else:
            return True
                
# Better code

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        
        mapping = {")":"(","]":"[","}":"{"}
        
        for ele in s:
            if ele in mapping:
                temp = arr.pop() if arr else '#'
                if(mapping[ele] != temp):
                    return False
            else:
                arr.append(ele)
        
        return not arr
        
                