class Solution(object):
    def findKthSmallest(self, coins, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def lcm(a, b):
            return a * b // gcd(a, b)
            
        n = len(coins)
        lcm_data = []
        for i in range(1, 1 << n):
            curr_lcm = 1
            bits = 0
            for j in range(n):
                if i & (1 << j):
                    curr_lcm = lcm(curr_lcm, coins[j])
                    bits += 1
            sign = 1 if bits % 2 == 1 else -1
            lcm_data.append((curr_lcm, sign))
        def count_multiples(x):
            res = 0
            for l, sign in lcm_data:
                res += sign * (x // l)
            return res
        left = 1
        right = min(coins) * k
        
        while left < right:
            mid = left + (right - left) // 2
            if count_multiples(mid) < k:
                left = mid + 1
            else:
                right = mid
                
        return left