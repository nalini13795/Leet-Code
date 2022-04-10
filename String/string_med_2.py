'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        temp ={}
        ans = 0
        while(end<len(s)):
            if(s[end] in s[start:end]):
                start = temp[s[end]]+1
                temp[s[end]] = end
                end+=1
            else:
                temp[s[end]] = end
                end+=1
                ans = max(len(s[start:end]),ans)
        return ans
                
            
            
            
        