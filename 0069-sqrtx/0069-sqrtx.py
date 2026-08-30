class Solution(object):
    def mySqrt(self, x):
        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
                
        return right