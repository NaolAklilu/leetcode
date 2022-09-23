class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        if len(num) <= k:
            return "0"
        
        for char in num:
            while stack and k and int(stack[-1]) > int(char):
                stack.pop()
                k -= 1
                
            stack.append(char)
        
        while len(stack) > 1 and int(stack[0]) == 0:
            stack.pop(0)
        
        if k > 0:
            stack = stack[0:-k]
                
        return "".join(stack) if stack else "0"
            
