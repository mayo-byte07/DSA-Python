class Solution(object):
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(current_str, open_count, close_count):
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
                
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return res