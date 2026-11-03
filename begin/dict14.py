n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
w = int(input())
for k in list(d):
    if d[k] < w:
        del d[k]
print(len(d))
