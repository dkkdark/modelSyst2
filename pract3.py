import multMethod as mm

n1 = 10**2
n2 = 10**3
n3 = 10**4
n4 = 10**5
A = 0
B = 10
x0 = 1

res = mm.multMethod(n1, A, B, x0)
res2 = mm.multMethod(n2, A, B, x0)
res3 = mm.multMethod(n3, A, B, x0)
res4 = mm.multMethod(n4, A, B, x0)

M1 = sum(res) / n1
sqRes1 = 0
for i in res:
    sqRes1 += i**2
D1 = (sqRes1 / n1 - M1**2) * n1 / (n1-1)

M2 = sum(res2) / n2
sqRes2 = 0
for i in res2:
    sqRes2 += i**2
D2 = (sqRes2 / n2 - M2**2) * n2 / (n2-1)

M3 = sum(res3) / n3
sqRes3 = 0
for i in res3:
    sqRes3 += i**2
D3 = (sqRes3 / n3 - M3**2) * n3 / (n3-1)

M4 = sum(res4) / n4
sqRes4 = 0
for i in res4:
    sqRes4 += i**2
D4 = (sqRes4 / n4 - M4**2) * n4 / (n4-1)


MT = (B - A) / 2
# DT = (sqRes2 /n4 - MT**2)

print("Мат ожидания:")
print(M1)
print(M2)
print(M3)
print(M4)
print(MT)
print("Десперсия:")
print(D1)
print(D2)
print(D3)
print(D4)
