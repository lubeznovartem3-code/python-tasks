m = int(input())
n = int(input())
v = [int(x) for x in input().split()]
a = []
for i in range(m):
    a.append(v[:])
for r in a:
    print(r)
