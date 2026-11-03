import math


def triangle_ps(a):
    return 3 * a, a * a * math.sqrt(3) / 4


for i in range(3):
    a = float(input())
    p, s = triangle_ps(a)
    print(p)
    print(s)
