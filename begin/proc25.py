def is_square(k):
    r = int(k ** 0.5)
    return r * r == k or (r + 1) * (r + 1) == k


c = 0
for i in range(10):
    k = int(input())
    if is_square(k):
        c += 1
print(c)
