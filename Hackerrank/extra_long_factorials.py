def extraLongFactorials(n):
    step = result = 1
    while step <= n:
        result *= step
        step += 1
    return result


print(extraLongFactorials(25))
