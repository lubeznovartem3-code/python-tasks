n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
s = 0
for v in d.values():
    s = s + v
print(s)
