def digit_count_sum(k):
    c = 0
    s = 0
    while k > 0:
        s += k % 10
        c += 1
        k //= 10
    return c, s


for i in range(5):
    k = int(input())
    c, s = digit_count_sum(k)
    print(c)
    print(s)
