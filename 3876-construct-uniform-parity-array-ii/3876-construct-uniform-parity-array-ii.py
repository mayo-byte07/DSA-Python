class Solution(object):
    def uniformArray(self, nums1):
        min_val = min(nums1)
        if min_val % 2 != 0:
            return True
        for num in nums1:
            if num % 2 != 0:
                return False
                
        return True