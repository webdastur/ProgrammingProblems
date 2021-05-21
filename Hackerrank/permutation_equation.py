def permutationEquation(p):
    result = []
    for i in range(1, len(p) + 1):
        item_index = p.index(i)
        result.append(p.index(item_index + 1) + 1)
    return result


print(permutationEquation([4, 3, 5, 1, 2]))
