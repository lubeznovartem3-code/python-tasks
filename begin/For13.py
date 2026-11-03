n = int(input())
s = 0
x = 1.1
sign = 1
for i in range(n):
    s += sign * x
    x += 0.1
    sign = -sign
print(s)