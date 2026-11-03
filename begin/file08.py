a = input()
b = input()
with open(a, encoding="utf-8") as f:
    x = [int(line) for line in f if line.strip()]
with open(b, "w", encoding="utf-8") as f:
    f.write(str(x[0]) + "\n")
    f.write(str(x[-1]) + "\n")
