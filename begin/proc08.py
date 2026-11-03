def add_right_digit(d, k):
    return k * 10 + d


k = int(input())
a = int(input())
b = int(input())
k = add_right_digit(a, k)
print(k)
k = add_right_digit(b, k)
print(k)
