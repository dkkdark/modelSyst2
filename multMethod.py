a = 22695477
b = 1
m = 2**32

def multMethod(n, A, B, x0):
    arr = [(a * x0 + b) % m]
    for i in range(1, n):
        arr.append((a * arr[i-1] + b) % m)

    res = []
    for el in arr:
        xmi = el / m
        x = int((B-A) * xmi + A)
        res.append(x)

    return res


"""
Функция для 5 и 6 заданий
"""
# Выводит массив, в котором индекс - случайное число, а значение - число его повторений
def freqNumbers(res, A, B, m, n):
    S = (B - A) / m
    freq = []
    for i in range(0, m-1):
        freq = [0] * m
        for j in range(0, len(res)):
            t = int(res[j]/S)
            freq[t] = freq[t] + 1
    res = [x / n for x in freq]
    return res