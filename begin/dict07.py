n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
b = None
for k in d:
    if b is None or d[k] > d[b]:
        b = k
print(b)
