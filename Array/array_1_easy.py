"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


# def two_sum(nums, target):
#         for i in range(0,len(nums)):
#             temp = nums[i]
#             for j in range(i+1, len(nums)):
#                 if(temp + nums[j] == target):
#                     return [i,j]

# nums = [2,7,11,15] 
# target = 9
# print(two_sum(nums,target))

# Can be solved with Hash table with O(N)

def two_sum_hashmap(nums, target):
    hashmap = {}
    for i in range(0,len(nums)):
        hashmap[nums[i]] = i
    
    for i in range(0,len(nums)):
        compl = target - nums[i]
        if(compl in hashmap and hashmap[compl]!= i):
            return[i,hashmap[compl]]

nums = [2,7,11,15] 
target = 10
print(two_sum_hashmap(nums,target))