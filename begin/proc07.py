def invert_digits(k):
    r = 0
    while k > 0:
        r = r * 10 + k % 10
        k //= 10
    return r


for i in range(5):
    k = int(input())
    print(invert_digits(k))
