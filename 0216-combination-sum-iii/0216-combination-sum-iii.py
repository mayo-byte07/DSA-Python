class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        def backtrack(start, current_sum, path):
            if len(path) == k:
                if current_sum == n:
                    res.append(list(path))
                return
            for i in range(start, 10):
                if current_sum + i > n:
                    break
                path.append(i)
                backtrack(i + 1, current_sum + i, path)
                path.pop()
        backtrack(1, 0, [])
        return res