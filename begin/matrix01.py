m = int(input())
n = int(input())
a = []
for i in range(1, m + 1):
    r = []
    for j in range(n):
        r.append(10 * i)
    a.append(r)
for r in a:
    print(r)
