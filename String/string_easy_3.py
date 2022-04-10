'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

'''
#using Hash Table O(n)

class Solution(object):
    def create_char_count(self,s):
        char_count_word = {}
        for ele in s:
            if(ele in char_count_word.keys()):
                char_count_word[ele] +=1
            else:
                char_count_word[ele] = 1
        return char_count_word
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        
        char_count_word = self.create_char_count(s)
        char_count_ana = self.create_char_count(t)
        for key, val in char_count_word.items():
            if(key not in char_count_ana.keys()):
                return False
            elif(char_count_ana[key] != char_count_word[key]):
                return False
        return True
        
#using Array and sorting O(nlogn)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(sorted(s) == sorted(t)):
            return True
        else:
            return False
        