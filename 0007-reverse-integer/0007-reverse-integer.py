class Solution(object):
    def reverse(self, x):
        INT_MAX = 2147483647  # 2^31 - 1
        
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > 7):
                return 0
                
            res = res * 10 + pop
            
        return res * sign