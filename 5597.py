s = list(range(1,31))
while len(s)>2:
    a = int(input())
    try:
        s.remove(a)
    except:
        continue
for i in range(len(s)): print(s[i])