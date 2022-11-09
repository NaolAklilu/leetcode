class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = 1
        temp = a
        
        for i in range(len(b)):
            if b[i] not in a:
                return -1
        
        while len(a) <= 10**4:
            if len(a) < len(b):
                times += 1
                a= temp*times
            else:
                if b in a:
                    return times
                times += 1
                a = temp*(times)
        return -1
      
