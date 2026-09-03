class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum = 0
        curr_max = 0
        max_sum = float('-inf')
        curr_min = 0
        min_sum = float('inf')
        for num in nums:
            total_sum += num
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)