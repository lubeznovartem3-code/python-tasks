n = int(input())
a = []
for i in range(n):
    x = float(input())
    y = float(input())
    a.append([x, y])
a.sort(key=lambda r: r[0], reverse=True)
for r in a:
    print(r)
print(a[0])
