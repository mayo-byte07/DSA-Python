class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = []
        i = 0
        j = 0
        
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
            
        # Append any remaining characters from either string
        res.append(word1[i:])
        res.append(word2[j:])
        
        return "".join(res)