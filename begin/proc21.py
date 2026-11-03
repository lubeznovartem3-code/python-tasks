def sum_range(a, b):
    if a > b:
        return 0
    s = 0
    for i in range(a, b + 1):
        s += i
    return s


a = int(input())
b = int(input())
c = int(input())
print(sum_range(a, b))
print(sum_range(b, c))
