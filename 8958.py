t = int(input())

def sumAll(s):
    ssumall = 0
    for i in range(0, len(s)):
        ssumall += i+1
        
    return ssumall

for i in range(t):
    ssum = 0
    a = input().split('X')
    for s in a:
        ssum += sumAll(s)
        
    print(ssum)