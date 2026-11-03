m = int(input())
n = int(input())
a = []
for i in range(m):
    r = []
    for j in range(1, n + 1):
        r.append(5 * j)
    a.append(r)
for r in a:
    print(r)
