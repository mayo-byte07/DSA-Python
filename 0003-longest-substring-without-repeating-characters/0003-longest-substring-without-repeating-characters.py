class Solution(object):
    def lengthOfLongestSubstring(self,s):
        char_map = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in char_map:
                left = max(left, char_map[char] + 1)
            char_map[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len