def jumpingOnClouds(c, k):
    energy = 100
    i = k % len(c)
    energy -= c[i] * 2 + 1
    while i != 0:
        i = (i + k) % len(c)
        energy -= c[i] * 2 + 1
    return energy


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
