# Begin18. Даны три точки A, B, C на числовой оси. Точка C расположена между А и В. Найти произведение длин отрезков AC и BC.
a = float(input())
b = float(input())
c = float(input())

ac = abs(c - a)
bc = abs(c - b)
product = ac * bc

print(product)
