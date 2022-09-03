class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = sorted(s)
        string2 = sorted(t)
        
        if len(string1) != len(string2):
            return False
        
        for i in string1:
            if i in string2:
                string2.remove(i)
        
        if len(string2) == 0:
            return True
        else: 
            return False
