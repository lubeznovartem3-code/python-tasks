a = input()
b = input()

c = 0

try:
    if a != float(a) or b != float(b):
        raise ValueError("нужно вводить цифры")
    if b == 0:
        raise ValueError("нельзя делить на ноль")
    c = a / b
    print(f"Результат: {c:.2b}")
except ValueError as e:
    if "could not convert string to float" in str(e):
        print("Так не получится: нужно вводить цифры")
    else:    
        print(f"Так не получится: {e}")