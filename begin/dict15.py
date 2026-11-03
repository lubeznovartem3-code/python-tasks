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
c = 0
for k in b:
    if k in a:
        c = c + 1
    else:
        a[k] = b[k]
print(len(a))
print(c)
