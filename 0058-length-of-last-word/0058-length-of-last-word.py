class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])