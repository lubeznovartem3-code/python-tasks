m = int(input())
n = int(input())
q = int(input())
v = [int(x) for x in input().split()]
a = []
for i in range(m):
    a.append([x * q ** i for x in v])
for r in a:
    print(r)
