# def reachingPoints( a, b, c, d):
#         while a <= c and b <= d:
#             if c == a and d == b: 
#                 return 'YES'
#             if c == d: break
#             if c > d:
#                 c %= d
#             elif d > c:
#                 d %= c
            
#             if c == a: # only change d
#                 if (d-b) % a ==0:
#                     return 'Yes'
#                 else:
#                     return 'NO' 
                
#             if d == b: # only change c
#                 if (c-a) % b == 0:
#                     return 'YES'
#                 else:
#                     return 'NO' 
#         return 'NO' 

# print(reachingPoints(1,2,3,6))

def sum_diff(x):
    sum = 0
    for i in range(1,len(x)):
        if(i%2==0):
            sum += x[i-1]
        else:
            sum -= x[i-1]
    return sum
a =[0, 1, 0, 0]
print(sum_diff(a))