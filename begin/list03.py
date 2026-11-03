n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = 0
p = 1
for i in range(len(a)):
    s = s + a[i]
    if i % 2 == 0:
        p = p * a[i]
print(s)
print(p)
