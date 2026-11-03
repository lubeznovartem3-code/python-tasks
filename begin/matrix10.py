m = int(input())
n = int(input())
a = []
for i in range(m):
    a.append([int(x) for x in input().split()])
for j in range(0, n, 2):
    for r in a:
        print(r[j])
