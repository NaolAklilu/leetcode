class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack.append([char, stack[-1][1]+1])
            
            else:
                stack.append([char, 1])
            
            if stack[-1][1] == 2:
                for _ in range(2):
                    stack.pop()
            
        res = []
        for i in range(len(stack)):
            res.append(stack[i][0])
        
        return "".join(res)
