a = int(input())
b = int(input())
c = int(input())
sol = a*b*c

for i in range(10):
    print(str(sol).count(f'{i}'))