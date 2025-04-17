num = int(input())
if num < 5:
    print("few")
elif num < 10:
    print("several")
elif num < 20:
    print("pack")
elif num < 50:
    print("lots")
elif num < 100:
    print("horde")
elif num < 250:
    print("throng")
elif num < 500:
    print("swarm")
elif num < 1000:
    print("zounds")
else:
    print("legion")