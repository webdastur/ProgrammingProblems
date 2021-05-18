def countingValleys(steps: int, path: str):
    valleys = 0
    altitude = 0
    for i in path:
        if i == 'U':
            altitude += 1
        else:
            altitude -= 1
        if altitude == 0 and i == 'U':
            valleys += 1
    return valleys


print(countingValleys(8, 'UDDDUDUU'))
