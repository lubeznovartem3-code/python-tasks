n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
q = input()
d.pop(q, None)
print(len(d))
