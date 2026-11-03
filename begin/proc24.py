def even(k):
    return k % 2 == 0


c = 0
for i in range(10):
    k = int(input())
    if even(k):
        c += 1
print(c)
