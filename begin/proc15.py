def shift_left3(a, b, c):
    return b, c, a


for i in range(2):
    a = float(input())
    b = float(input())
    c = float(input())
    x, y, z = shift_left3(a, b, c)
    print(x)
    print(y)
    print(z)
