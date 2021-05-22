def saveThePrisoner(n, m, s):
    return ((s - 1 + m - 1) % n) + 1


print(saveThePrisoner(7, 19, 2))
