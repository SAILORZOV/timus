accounts = set()
spammers = set()
for i in range(int(input())):
    a = input()
    if a in accounts:
        spammers.add(a)
    else:
        accounts.add(a)
for i in spammers:
    print(i)