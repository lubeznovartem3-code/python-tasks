n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
print(len(d))
for k in d:
    print(k)
