s = input()
c = 0
for x in s:
    if "a" <= x <= "z" or "а" <= x <= "я":
        c += 1
print(c)
