t = int(input())
tests = [map(int, input().split()) for x in range(t)]

def findRoom(h,w,n):
    f = h if n%h == 0 else n%h
    r = int(n/h) if n%h == 0 else int(n/h)+1
    r = format(r, '02') 
    return f'{f}{r}'
    

for h,w,n in tests:
    print(findRoom(h,w,n))