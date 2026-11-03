n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = [x for x in a if x > 0]
print(b)
print(len(b))
