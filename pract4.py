import multMethod as mm

n1 = 10**2
n2 = 10**3
n3 = 10**4
n4 = 10**5
A = 0
B = 10
x0 = 1

res1 = mm.multMethod(n1, A, B, x0)
res2 = mm.multMethod(n2, A, B, x0)
res3 = mm.multMethod(n3, A, B, x0)
res4 = mm.multMethod(n4, A, B, x0)


def period(n, res):
    for i in range(0, n):
        for j in range(i+1, n):
            if res[i] == res[j]:
                return j-i
    return -1


print(period(n4, res4))
