def pyramid_pattern(rows):
    for i in range(rows):

        for j in range(rows - i - 1):
            print(' ', end='')

        for k in range(2 * i + 1):
            print(chr(65 + k), end='')

        print()


n = 8

pyramid_pattern(n)


def pyramid_pattern_rv(rows):
    for i in range(rows):

        for j in range(i):
            print(' ', end='')

        for j in range(2 * (rows - i) - 1):
            print(chr(65 + j), end='')

        print()


n = 8

pyramid_pattern_rv(n)
