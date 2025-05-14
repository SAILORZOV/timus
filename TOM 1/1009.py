N = int(input())
K = int(input())

nums = {(0, 0): 0, (0, 1): K - 1}
for i in range(1, N):
    nums[(i, 0)] = nums[(i - 1, 1)]
    nums[(i, 1)] = (nums[(i - 1, 0)] + nums[(i - 1, 1)]) * (K - 1)


print(nums[(N - 1, 0)] + nums[(N - 1, 1)])