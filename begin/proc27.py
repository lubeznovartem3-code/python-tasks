def is_power_n(k, n):
    while k % n == 0:
        k //= n
    return k == 1


n = int(input())
c = 0
for i in range(10):
    k = int(input())
    if is_power_n(k, n):
        c += 1
print(c)
