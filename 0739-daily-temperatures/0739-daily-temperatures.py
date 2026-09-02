class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Will store indices of the temperatures
        
        for i, temp in enumerate(temperatures):
            # While stack is not empty and current temp is greater than the temp at the index on top of the stack
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx
            
            stack.append(i)
            
        return answer