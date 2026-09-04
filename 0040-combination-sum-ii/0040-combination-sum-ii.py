class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        
        def backtrack(start, current_sum, path):
            if current_sum == target:
                res.append(list(path))
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                if current_sum + candidates[i] > target:
                    break
                    
                path.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], path)
                path.pop()
                
        backtrack(0, 0, [])
        return res