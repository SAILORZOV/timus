n = int(input())
letter_to_int = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def cells(s):
    count = 0
    ways = [-2, -1, 1, 2]
    a = int(letter_to_int[s[0]])
    b = int(s[1])

    for i in ways:
        for j in ways:
            if (i + j) % 2 == 0:
                continue
            if (0 < a + i < 9) and (0 < b + j < 9):
                count += 1
    return count


for i in range(n):
    print(cells(input()))
