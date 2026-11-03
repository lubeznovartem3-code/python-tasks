def digit_count(k):
    c = 0
    while k > 0:
        c += 1
        k //= 10
    return c


for i in range(5):
    k = int(input())
    print(digit_count(k))
