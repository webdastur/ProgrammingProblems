def squares(a, b):
    s = int(b ** .5) - int(a ** .5)
    return s + 1 if int(a ** .5) ** 2 == a else s


print(squares(3, 9))
print(squares(17, 24))
