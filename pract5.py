import multMethod as mm
"""
res1 - random numbers
A - left border
B - right border
m - number of plots
"""

A = 0
B = 10
m = 10

n1 = 10**2
x0 = 1
res1 = mm.multMethod(n1, A, B, x0)


print(mm.freqNumbers(res1, A, B, m))
