n = int(input())
sizes = list(map(int, input().split()))
t,p = map(int, input().split())

total_t = 0

for i in sizes:
    tn = i//t
    total_t = total_t+tn+1 if i%t > 0 else total_t+tn 

print(total_t)

total_pen = n//p
less_pen = n%p

print(total_pen, less_pen)

# short version

# N = int(input())
# t = list(map(int, input().split()))
# T, P = map(int, input().split())
# a = 0
# for s in t: a += s//T + bool(s%T)
# print(a)
# print(N//P, N%P)