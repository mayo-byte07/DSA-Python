class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        curr_sum = 0
        min_len = float('inf')
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
                
        return min_len if min_len != float('inf') else 0

# Follow-up: O(n log(n)) solution using Prefix Sums and Binary Search
"""
import bisect

class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        # Create a prefix sum array of size n + 1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        min_len = float('inf')
        
        for i in range(n):
            # We are looking for an index j such that prefix[j] - prefix[i] >= target
            # Therefore, prefix[j] >= target + prefix[i]
            to_find = target + prefix[i]
            bound = bisect.bisect_left(prefix, to_find)
            
            if bound <= n:
                min_len = min(min_len, bound - i)
                
        return min_len if min_len != float('inf') else 0
"""