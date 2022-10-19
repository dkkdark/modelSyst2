import multMethod as mm
import numpy as np
import matplotlib.pyplot as plt

A = 0
B = 10
m = 10

n1 = 10**2
n2 = 10**3
n3 = 10**4
n4 = 10**5
x0 = 1

res1 = mm.multMethod(n1, A, B, x0)
res2 = mm.multMethod(n2, A, B, x0)
res3 = mm.multMethod(n3, A, B, x0)
res4 = mm.multMethod(n4, A, B, x0)

fr1 = mm.freqNumbers(res1, A, B, m, n1)
fr2 = mm.freqNumbers(res2, A, B, m, n2)
fr3 = mm.freqNumbers(res3, A, B, m, n3)
fr4 = mm.freqNumbers(res4, A, B, m, n4)
print(fr1, fr2, fr3, fr4)

x = np.arange(1, 11)
fig, ax = plt.subplots(4, 1)

ax[0].bar(x, fr1)
ax[1].bar(x, fr2)
ax[2].bar(x, fr3)
ax[3].bar(x, fr4)

fig.set_figwidth(24)
fig.set_figheight(18)
#plt.show()


# Присон
nj = 1 / 10
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for i in fr1:
    sum1 += ((nj - i)**2)/i
for i in fr2:
    sum2 += ((nj - i)**2)/i
for i in fr3:
    sum3 += ((nj - i)**2)/i
for i in fr4:
    sum4 += ((nj - i)**2)/i
print(sum1, sum2, sum3, sum4)
