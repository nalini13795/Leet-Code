
'''
find the maximum sum of k unique elements in a list

'''

def findMaxSum(a, n):
    max = -1
    for ele in range(len(a)-n+1):
        s = set()
        temp = 0
        for i in range(n):
            s.add(a[ele + i])
            temp = a[ele + i] + temp
        
        if(max < temp  and len(s) == n):
            max = temp
    
    print(max)



a = [1,2,4,4]
findMaxSum(a,4)