'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for ele in strs:
            sorted_ele = "".join(sorted(ele))
            if(sorted_ele in hash_table.keys()):
                hash_table[sorted_ele].append(ele)
            else:
                hash_table[sorted_ele] = [ele]
        final = []
        for keys, values in hash_table.items():
            final.append(values)

        return final