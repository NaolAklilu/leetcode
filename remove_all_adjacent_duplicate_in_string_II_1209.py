class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack.append([char , stack[-1][1]+1])

            else:
                stack.append([char, 1])
            
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
            
        res = []   
        for i in range(len(stack)):
            res.append(stack[i][0])
                    
        return "".join(res)
