'''
Binary Search Tree

'''
def binarySearch(nums, target):
    high = len(nums) - 1
    low = 0
    while high >= low:
        mid = high + low // 2
        if(nums[mid]==target):
            return mid
        elif(nums[mid]>target):
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == '__main__':
 
    nums = [2, 5, 6, 8, 9, 10]
    target = 5
 
    index = binarySearch(nums, target)
 
    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')