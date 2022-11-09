class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 1
        while i < len(s):
            substring = s[:i]
            times = len(s)//i
            if substring*times == s:
                return True
            i +=1
            
        return False
    
        
