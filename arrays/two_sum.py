def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[i]+nums[j+i+1] == target:
                    return [i,j+i+1]
        return 