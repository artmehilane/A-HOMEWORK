from math import factorial



def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    parim = 0
    komb_arv = factorial(len(nums)) / (factorial(len(nums) - 3) * factorial(3))

    for a in range(len(nums) - 3):
        for b in range(1, len(nums) - 2):
            for c in range(2, len(nums) - 1):
                if a == 0 and b == 1 and c == 2:
                    parim = nums[a] + nums[b] + nums[c]
                    summa = nums[a] + nums[b] + nums[c]
                summa = nums[a] + nums[b] + nums[c]
                if abs(target - summa) < abs(target - parim):
                    parim = summa
                    print(nums[a], nums[b], nums[c])

    return parim

nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))
#comm
