class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        x = list(str(x))
        while int(x[-1]) == 0:
            x= x[:len(x)-1]
        
        if x[0] != "-":
            for i in range(len(x)//2):
                x[i], x[len(x)-i-1] = x[len(x)-i-1], x[i]
        else:
            x = x[1:]
            for i in range(len(x)//2):
                x[i], x[len(x)-i-1] = x[len(x)-i-1], x[i]
                
            x.insert(0, '-')
            
        x = "".join(x)
        if int(x) in range((-2)** 31, (2**31)-1):
            return x
        
        return 0 
