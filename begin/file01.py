s = input()
try:
    with open(s, "w", encoding="utf-8") as f:
        pass
    print(True)
except (OSError, ValueError):
    print(False)
