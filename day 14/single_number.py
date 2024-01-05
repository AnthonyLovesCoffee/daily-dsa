def singleNumber(nums):
        ans = {}
        for key in nums:
            if key in ans:
                ans[key] += 1
            else:
                ans[key] = 1
        for element,count in ans.items():
            if count == 1:
                return element
            
print(singleNumber([4,1,2,1,2]))