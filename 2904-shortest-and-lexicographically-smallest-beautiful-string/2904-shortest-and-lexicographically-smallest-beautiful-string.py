class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ans = ""
        min_len = float('inf')
        
        for i in range(len(s)):
            ones = 0
            for j in range(i, len(s)):
                if s[j] == '1':
                    ones += 1
                
                if ones == k:
                    sub = s[i:j+1]
                    if len(sub) < min_len:
                        min_len = len(sub)
                        ans = sub
                    elif len(sub) == min_len:
                        if sub < ans:
                            ans = sub
                elif ones > k:
                    break
                    
        return ans