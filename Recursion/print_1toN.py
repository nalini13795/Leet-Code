def printNto1(n):
    if(n==0):
        return 1
    print(n)
    printNto1(n-1)

def print1toN(n):
    if(n==0):
        return 1
    print1toN(n-1)
    print(n)

printNto1(8)
# print1toN(10)