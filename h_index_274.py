class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cited, length = 0, len(citations)
        res = [0] * (length + 1)
        
        for i in range(length):
            if citations[i] >= length:
                res[length] += 1
            else:
                res[citations[i]] += 1

        for i in range(len(res)-1, -1, -1):
            cited += res[i]
            res[i] = cited
            
        for i in range(len(res)-1, -1, -1):
            if res[i] >= i:
                return i
            
        return 0
    
