def is_equal(t1, t2):
    rotations = [
        (0, 1, 2, 3),
        (0, 2, 3, 1),
        (0, 3, 1, 2),
        (1, 0, 3, 2),
        (1, 2, 0, 3),
        (1, 3, 2, 0),
        (2, 0, 1, 3),
        (2, 1, 3, 0),
        (2, 3, 0, 1),
        (3, 0, 2, 1),
        (3, 1, 0, 2),
        (3, 2, 1, 0),
    ]

    for r in rotations:
        q = 0
        for i in range(4):
            if t1[i] == t2[r[i]]:
                q+=1
            else:
                break
        if q == 4:
            return True
    return False

if is_equal(input(), input()):
    print("equal")
else:
    print("different")