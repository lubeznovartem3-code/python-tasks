m = int(input())
n = int(input())
d = int(input())
v = [int(x) for x in input().split()]
a = []
for i in range(m):
    r = []
    for j in range(n):
        r.append(v[i] + d * j)
    a.append(r)
for r in a:
    print(r)
