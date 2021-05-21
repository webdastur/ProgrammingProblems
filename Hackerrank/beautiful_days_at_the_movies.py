def beautifulDays(i: int, j: int, k: int):
    count = 0
    for i in range(i, j + 1):
        if abs(i - int(str(i)[::-1])) % k == 0:
            count += 1
    return count


print(beautifulDays(13, 45, 3))
