n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
r = {}
for k, v in d.items():
    r[v] = k
for v, k in r.items():
    print(f"{v}: {k}")
