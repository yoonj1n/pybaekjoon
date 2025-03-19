def sol(a):
    return sum(list(map(lambda x : x*x, a)))%10

a = list(map(int, input().split()))
print(sol(a))