n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = 0
for i in range(len(a)):
    if a[i] > a[b]:
        b = i
print(b)
print(a[b])
