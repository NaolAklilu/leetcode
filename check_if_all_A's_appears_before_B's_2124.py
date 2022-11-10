class Solution:
    def checkString(self, s: str) -> bool:
        count_a, count_b = 0, 0
        
        for char in s:
            if char == 'a':
                if count_b != 0:
                    return False
                count_a += 1
            else:
                count_b += 1
        
        return True
                
