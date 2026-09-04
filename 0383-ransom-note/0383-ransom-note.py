class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
            
        counts = {}
        for char in magazine:
            counts[char] = counts.get(char, 0) + 1
        for char in ransomNote:
            if counts.get(char, 0) <= 0:
                return False
            counts[char] -= 1
            
        return True