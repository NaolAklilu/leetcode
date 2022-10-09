class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = []
        for i in range(1,n+1):
            lst.append(i) 
        
        def findCurWinner(lst):
            if len(lst) == 1:
                return lst[0]
            
            x = k
            while x>1:
                temp = lst.pop(0)
                lst.append(temp)
                x -= 1
            lst.pop(0)
            
            return findCurWinner(lst)
            
        return findCurWinner(lst)           
