def angryProfessor(k: int, a: list[int]) -> str:
    return 'NO' if list(map(lambda x: x <= 0, a)).count(True) >= k else 'YES'


print(angryProfessor(2, [0, -1, 2, 1]))
