import math


def triangle_p(a, h):
    b = math.sqrt((a / 2) ** 2 + h * h)
    return a + 2 * b


for i in range(3):
    a = float(input())
    h = float(input())
    print(triangle_p(a, h))
