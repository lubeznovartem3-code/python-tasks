n = int(input())
s = []
for i in range(n):
    s.append(input())
b = [len(x) for x in s]
print(b)
print(sum(b))
