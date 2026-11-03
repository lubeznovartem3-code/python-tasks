N = int(input())
current_sum = 0
K = 0

while current_sum + (K + 1) <= N:
    K += 1
    current_sum += K

print(f"Наибольшее K = {K}")
print(f"Сумма = {current_sum}")
