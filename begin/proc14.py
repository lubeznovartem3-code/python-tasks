def shift_right3(a, b, c):
    return c, a, b


for i in range(2):
    a = float(input())
    b = float(input())
    c = float(input())
    x, y, z = shift_right3(a, b, c)
    print(x)
    print(y)
    print(z)
