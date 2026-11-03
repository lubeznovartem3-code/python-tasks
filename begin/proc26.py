def is_power5(k):
    while k % 5 == 0:
        k //= 5
    return k == 1


c = 0
for i in range(10):
    k = int(input())
    if is_power5(k):
        c += 1
print(c)
