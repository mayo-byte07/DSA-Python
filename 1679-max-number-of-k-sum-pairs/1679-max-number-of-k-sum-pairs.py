class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        left = 0
        right = len(nums) - 1
        operations = 0
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
                
        return operations