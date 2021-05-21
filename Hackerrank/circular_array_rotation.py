def circularArrayRotation(a: list[int], k: int, queries: list[int]) -> list[int]:
    for i in range(k):
        popped_item = a.pop()
        a.insert(0, popped_item)
    return [a[x] for x in queries]


print(circularArrayRotation([3, 4, 5], 2, [1, 2]))
