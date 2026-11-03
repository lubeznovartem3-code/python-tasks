A = float(input())
current_sum = 0.0
K = 0

while current_sum <= A:
    K += 1
    current_sum += 1 / K

print(f"Наименьшее K = {K}")
print(f"Сумма = {current_sum:.6f}")
