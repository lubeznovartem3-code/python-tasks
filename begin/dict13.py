n = int(input())
d = {}
for i in range(n):
    k = input()
    p = int(input())
    q = int(input())
    d[k] = [p, q]
s = 0
b = None
for k in d:
    p, q = d[k]
    s = s + p * q
    if b is None or p * q > d[b][0] * d[b][1]:
        b = k
print(s)
print(b)
