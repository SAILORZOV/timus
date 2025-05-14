a = input()

word = [a[0]]
for i in range(1, len(a)):
    if word and word[-1] == a[i]:
        word.pop()
    else:
        word.append(a[i])

print(''.join(word))
