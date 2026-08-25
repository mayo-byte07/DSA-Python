class Solution(object):
    def isPalindromic(self, s):
        bin_str = "".join(format(ord(c), '08b') for c in s)
        return bin_str == bin_str[::-1]