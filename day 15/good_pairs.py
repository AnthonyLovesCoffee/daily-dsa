def numIdenticalPairs(nums):
    pair = 0
    num_count = {}
    for num in nums :
        if num in num_count :
            pair += num_count[num]
            num_count[num] += 1
        else :
            num_count[num] = 1
    return pair

print(numIdenticalPairs([1,2,3,1,1,3])) # return 4