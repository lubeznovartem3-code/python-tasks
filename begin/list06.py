n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
p = int(input())
q = int(input())
b = a[p:q + 1]
print(b)
s = 0
for x in b:
    s = s + x
print(s)
