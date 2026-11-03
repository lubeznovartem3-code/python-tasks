try:
    a=int(input())
    if a<0:
        raise ValueError("Не бывает отрицательного возраста")
    if a>120:
        raise ValueError("Да не живут столько")
    
    print("Четенько")
except ValueError as e:
    print(f"Незя такое: {e}")
