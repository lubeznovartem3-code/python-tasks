n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = sorted(a, reverse=True)
print(b[1])
