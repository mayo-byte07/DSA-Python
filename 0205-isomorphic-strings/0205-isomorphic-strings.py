class Solution(object):
    def isIsomorphic(self, s, t):
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))