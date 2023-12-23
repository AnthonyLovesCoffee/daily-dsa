## brute force, O(n^2)
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return []

## using hash map, O(n)
def twoSumHash(nums, target):
    numMap = {}
    n = len(nums)
    for i in range(n):
        numMap[nums[i]] = i

    # find the complement
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]

    return []  # no solution

print(twoSum([2,7,11,15], 9)) # expected [0,1]
print(twoSumHash([3,2,4], 6)) # expected [1,2]
