def findDigits(n: int) -> int:
    count = 0
    for digit in str(n):
        digit = int(digit)
        if digit != 0:
            if n % digit == 0:
                count += 1
    return count


for i in [12, 1012]:
    print(findDigits(i))
