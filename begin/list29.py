n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
b = sorted(a, reverse=True)
print(b[:k])
