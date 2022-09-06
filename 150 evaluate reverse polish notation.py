class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+' , '-' , '*', '/']
        
        for element in tokens:
            if element not in operators:
                stack.append(element)
            elif element in operators:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                
                if element == '+':
                    stack.append(num2 + num1)
                elif element == '-':
                    stack.append(num2 - num1)
                elif element == '*':
                    stack.append(num2 * num1)
                elif element == '/':
                    if num2 / num1 < 0:
                        stack.append(math.ceil(num2 / num1))
                    else:
                        stack.append(num2 // num1)             
                    
        return stack[0]
