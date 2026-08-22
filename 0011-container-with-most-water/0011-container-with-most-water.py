class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_height = min(height[left], height[right])
            current_width = right - left
            max_area = max(max_area, current_height * current_width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area