def utopianTree(n):
    h = 0
    for i in range(n + 1):
        if i % 2 == 0:
            h += 1
        else:
            h *= 2
    return h


print(utopianTree(4))
