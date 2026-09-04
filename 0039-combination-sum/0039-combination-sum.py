class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()        
        def backtrack(start, current_sum, path):
            if current_sum == target:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                if current_sum + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i, current_sum + candidates[i], path)
                path.pop()
                
        backtrack(0, 0, [])
        return res