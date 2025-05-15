a = 256 ** 3
b = 256 ** 2
c = 256
d = 1

i = input()
i = int(input())

aa = i // a
i -= aa * a
bb = i // b
i -= bb * b
cc = i // c
i -= cc * c
dd = i // d
i -= dd * d

print(dd * a + cc * b + bb * c + aa * d)
