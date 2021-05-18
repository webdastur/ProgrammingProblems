def catAndMouse(x: int, y: int, z: int) -> str:
    if abs(z - x) == abs(y - z):
        return "Mouse C"
    elif abs(z - x) > abs(z - y):
        return "Cat B"
    else:
        return "Cat A"


q = 2
inputs = [[1, 2, 3], [1, 3, 2]]

for i in range(q):
    print(catAndMouse(*inputs[i]))
