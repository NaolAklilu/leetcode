class Solution:
    def reverseParentheses(self, s: str) -> str:
        string = list(s)
        
        temp = []
        string_stack = []
        for char in string:
            if char != ')':
                string_stack.append(char)
            elif char == ')':
                keep = True
                temp = []
                while keep:
                    if string_stack[-1] != '(':
                        temp.append(string_stack.pop())
                        keep = True
                    else:
                        string_stack.pop()
                        keep = False
                string_stack = string_stack + temp
            
        return ''.join(string_stack)
