def power_a234(a):
    return a ** 2, a ** 3, a ** 4


for i in range(5):
    a = float(input())
    b, c, d = power_a234(a)
    print(b)
    print(c)
    print(d)
