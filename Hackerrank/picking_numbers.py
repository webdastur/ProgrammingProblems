def pickingNumbers(a: list) -> int:
    max_item = 0
    for i in a:
        left = a.count(i)
        right = a.count(i - 1)
        left = left + right
        if left > max_item:
            max_item = left
    return max_item


print(pickingNumbers([4, 6, 5, 3, 3, 1]))
