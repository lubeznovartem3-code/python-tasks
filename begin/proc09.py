def digit_count(k):
    c = 0
    while k > 0:
        c += 1
        k //= 10
    return c


def add_left_digit(d, k):
    return d * 10 ** digit_count(k) + k


k = int(input())
a = int(input())
b = int(input())
k = add_left_digit(a, k)
print(k)
k = add_left_digit(b, k)
print(k)
