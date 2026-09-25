# Begin15. Дана площадь S круга. Найти его диаметр D и длину L окружности. S = pi*R**2 -> R = (S/pi)**0.5 -> D = 2*R. pi = 3.14.
area = float(input())
pi = 3.14

r = (area / pi) ** 0.5
d = 2 * r
length = 2 * pi * r

print(d)
print(length)
