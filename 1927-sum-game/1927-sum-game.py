class Solution(object):
    def sumGame(self, num):
        n = len(num)
        sum_l = sum_r = 0
        cnt_l = cnt_r = 0
        
        half = n // 2
        for i in range(half):
            if num[i] == '?':
                cnt_l += 1
            else:
                sum_l += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                cnt_r += 1
            else:
                sum_r += int(num[i])
                
        return (sum_l - sum_r) * 2 != (cnt_r - cnt_l) * 9