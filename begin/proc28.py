def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


c = 0
for i in range(10):
    k = int(input())
    if is_prime(k):
        c += 1
print(c)
