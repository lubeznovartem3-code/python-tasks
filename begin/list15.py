n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = []
for i in range(1, len(a), 2):
    b.append(a[i])
print(b)
print(sum(b))
