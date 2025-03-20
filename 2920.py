a = list(map(int, input().split()))
sortA = sorted(a)
desortA = sorted(a,reverse=True)
if a == sortA:
    print('ascending')
elif a == desortA:
    print('descending')
else:
    print('mixed')