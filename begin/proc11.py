def minmax(x, y):
    if x < y:
        return x, y
    return y, x


a = float(input())
b = float(input())
c = float(input())
d = float(input())
p, q = minmax(a, b)
r, s = minmax(c, d)
lo, x = minmax(p, r)
y, hi = minmax(q, s)
print(lo)
print(hi)
