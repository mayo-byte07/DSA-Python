class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                if i % 2 == 0:
                    nums.pop(i)
                else:
                    nums.remove(nums[i])
            else:
                i += 1
        return len(nums)