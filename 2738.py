n,m = map(int, input().split())
a,b = [],[]
for i in range(n): #n개의 줄 a입력
    a.append(list(map(int, input().split())))

for i in range(n): #n개의 줄 b입력
    b.append(list(map(int, input().split())))

for i in range(n):
    for k in range(m):
        print(a[i][k]+b[i][k], end=' ')
    print()