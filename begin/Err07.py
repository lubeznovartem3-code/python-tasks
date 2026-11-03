while True:
    a=input()
    try:
        a=int(a)
    except ValueError:
        print("Целое число недо")
        continue
    print("Четенько")
    break