def sockMerchant(n: int, ar: list):
    return sum([ar.count(x) // 2 for x in set(ar) if ar.count(x) >= 2])


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))
