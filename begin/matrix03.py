m = int(input())
n = int(input())
v = [int(x) for x in input().split()]
a = []
for i in range(m):
    a.append([v[i]] * n)
for r in a:
    print(r)
