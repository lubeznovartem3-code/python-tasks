n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
m = sum(a) / len(a)
print([x for x in a if x > m])
print(m)
