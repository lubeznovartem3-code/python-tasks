import math


def mean(x, y):
    return (x + y) / 2, math.sqrt(x * y)


a = float(input())
b = float(input())
c = float(input())
d = float(input())
for x in [b, c, d]:
    p, q = mean(a, x)
    print(p)
    print(q)
