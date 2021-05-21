def hurdleRace(k, height: list) -> int:
    max_height = max(height)
    if max_height > k:
        return max_height - k
    else:
        return 0


print(hurdleRace(7, [2, 5, 4, 5, 2]))
