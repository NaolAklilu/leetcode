class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        next_warmer_temp = [0] * size
        stack = []
        
        for i in range(0,size):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                last_index = stack.pop()
                next_warmer_temp[last_index] = i - last_index
                
            stack.append(i)
        return next_warmer_temp
