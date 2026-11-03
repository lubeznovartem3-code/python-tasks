n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = [x * x for x in a]
print(b)
print(sum(b))
