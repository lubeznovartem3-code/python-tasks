N = int(input("Введите число N: "))

K = 1
while K * K <= N:
    K += 1

print(f"Наименьшее число K: {K}")
