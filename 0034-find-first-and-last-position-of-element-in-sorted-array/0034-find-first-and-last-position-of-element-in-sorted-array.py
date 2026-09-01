class Solution(object):
    def searchRange(self, nums, target):
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Continue searching left
                    else:
                        left = mid + 1   # Continue searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        return [findBound(True), findBound(False)]