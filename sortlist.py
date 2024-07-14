class sortList:
    def findCorrectPosition(self, nums, target):
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
            return len(nums)


item = sortList()
print(item.findCorrectPosition([1, 3, 5, 6], 2))
