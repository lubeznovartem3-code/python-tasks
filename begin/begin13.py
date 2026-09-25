# Begin13. Даны два круга с общим центром и радиусами R1 и R2 (R1 > R2). Найти площади кругов S1, S2 и кольца S3. pi = 3.14.
r1 = float(input())
r2 = float(input())
pi = 3.14

s1 = pi * (r1 ** 2)
s2 = pi * (r2 ** 2)
s3 = s1 - s2

print(s1)
print(s2)
print(s3)
