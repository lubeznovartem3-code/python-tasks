n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
m = sum(a) / len(a)
b = []
for x in a:
    if x > m:
        b.append(x)
print(b)
print(len(b))
