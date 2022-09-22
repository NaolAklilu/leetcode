class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_pointer = 0
        stack = []
        
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[pop_pointer]:
                stack.pop()
                pop_pointer += 1
                
        return True if len(stack) == 0 else False
