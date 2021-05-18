def getMoneySpent(keyboards: list, drives: list, b: int) -> int:
    can_buy_both = False
    m = 0
    for i in keyboards:
        for j in drives:
            if m < i + j <= b:
                m = i + j
                can_buy_both = True
    return m if can_buy_both else -1


print(getMoneySpent([4], [5], 5))
