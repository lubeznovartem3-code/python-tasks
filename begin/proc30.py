def digit_n(k, n):
    p = 1
    while k > 0:
        if p == n:
            return k % 10
        k //= 10
        p += 1
    return -1


for i in range(5):
    k = int(input())
    for n in range(1, 6):
        print(digit_n(k, n))
