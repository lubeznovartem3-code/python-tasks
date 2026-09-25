# Begin6. Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a*b*c и площадь поверхности S = 2*(a*b + b*c + a*c).
a = float(input())
b = float(input())
c = float(input())

volume = a * b * c
surface_area = 2 * (a * b + b * c + a * c)

print(volume)
print(surface_area)
