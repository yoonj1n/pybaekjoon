t = int(input())
for i in range(t):
    n,s = input().split()
    for k in range(len(s)):
        print(f'{s[k]}'*int(n),end='')
    print()
    
# batter
# t = int(input())
# for i in range(t):
#     n,s = input().split()
#     for k in s:
#         print(f'{k}'*int(n),end='')
#     print()
