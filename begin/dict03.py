n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
q = input()
print(d.get(q, 0))
