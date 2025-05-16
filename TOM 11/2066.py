import math


def find_min(a, b, c):
    nums = [a, b, c]
    minimum = math.inf
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(3):
                if i == k or j == k:
                    continue
                computed_nums = [nums[i] + nums[j] + nums[k], nums[i] + nums[j] - nums[k], nums[i] + nums[j] * nums[k],
                                 nums[i] - nums[j] + nums[k], nums[i] - nums[j] - nums[k], nums[i] - nums[j] * nums[k],
                                 nums[i] * nums[j] + nums[k], nums[i] * nums[j] - nums[k], nums[i] * nums[j] * nums[k]]
                minimum = min(minimum, min(computed_nums))
    return minimum


a = int(input())
b = int(input())
c = int(input())

print(find_min(a, b, c))
