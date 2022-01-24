'''
input = "AZB"
output = 1+2 = 3
'''
import string

def getTime(s):
    s = s.lower()
    alpha_to_int = dict(zip(string.ascii_lowercase, range(1,27)))
    res = 0
    for i in range(1,len(s)):
        diff = abs(alpha_to_int[s[i-1]]-alpha_to_int[s[i]])
        if(diff>13):
            res += 26 - diff
        else:
            res += diff

    print(res)

getTime('AzD')