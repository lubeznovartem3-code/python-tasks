n = int(input())
a = {}
for i in range(n):
    k = input()
    v = int(input())
    a[k] = v
m = int(input())
b = {}
for i in range(m):
    k = input()
    v = int(input())
    b[k] = v
c = ""
for k in a:
    if k in b:
        c = k
a.update(b)
print(len(a))
print(a[c])
