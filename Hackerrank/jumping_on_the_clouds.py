def jumpingOnClouds(c):
    jumps = 0
    current = 0
    n = len(c) - 1
    while current != n:
        # max jump
        jump = 2 if current + 2 <= n else 1

        if jump == 1:
            if c[current + jump] == 1:
                jump += 1
        else:
            if c[current + jump] == 1:
                jump -= 1

        current += jump
        jumps += 1

    return jumps


if __name__ == '__main__':
    print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
    print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
