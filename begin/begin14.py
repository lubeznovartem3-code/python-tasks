# Begin14. Дана длина L окружности. Найти ее радиус R и площадь S круга. L = 2*pi*R -> R = L / (2*pi). pi = 3.14.
length = float(input())
pi = 3.14

r = length / (2 * pi)
area = pi * (r ** 2)

print(r)
print(area)
