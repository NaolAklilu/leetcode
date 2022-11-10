class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s)
        num = []
        is_negative = False
        
        for i in range(len(s)):
            if len(num) == 0:
                if s[i] == "-":
                    if i+1 < len(s) and s[i+1].isnumeric():
                        is_negative = True
                    else:
                        return 0
                elif s[i] == " ":
                    continue
                elif s[i] == "+":
                    if i+1 < len(s) and s[i+1].isnumeric():
                        continue
                    else:
                        return 0
                elif s[i].isnumeric():
                    num.append(s[i])
                else:
                    return 0
                
            else:
                if s[i].isnumeric():
                    num.append(s[i])
                else:
                    break
            
        if is_negative == True:
            num.insert(0, "-")
            num = int("".join(num))
            if num not in range((-2)**31, (2**31)-1):
                num = max((-2)**31, min(num, (2**31)-1))
            return str(num)
        
        if len(num) == 0:
            return 0
        num = int("".join(num))
        if num not in range((-2)**31, (2**31)-1):
            num = max((-2)**31, min(num, (2**31)-1))
        return str(num)            
        
