'''
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

O(n) O(n)
'''
arg1 = [-1, -2, -3, -4, -5]
arg2 = -8


def twoSum(nums, target):
    myDict = dict()

    for i in range(len(nums)):
        if nums[i] in myDict:
            return [myDict[nums[i]], i]
        else:
            temp = target - nums[i]
            myDict[temp] = i

    return []


print(twoSum(arg1, arg2))
