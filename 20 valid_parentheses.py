class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        if len(s) == 1:
            return False
        else:
            for i in s:
                if i in dic.keys():
                    stack.append(i)
                elif i in dic.values():
                    if len(stack) == 0:
                        return False
                    else:
                        opening = stack.pop()
                        if dic[opening] != i:
                            return False
        if len(stack) == 0:
            return True
        else:
            return False
