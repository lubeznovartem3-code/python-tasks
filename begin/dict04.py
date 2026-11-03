n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
q = input()
w = int(input())
if q in d:
    d[q] = d[q] + w
else:
    d[q] = w
print(d[q])
