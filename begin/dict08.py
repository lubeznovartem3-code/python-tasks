n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
w = int(input())
print(w in d.values())
