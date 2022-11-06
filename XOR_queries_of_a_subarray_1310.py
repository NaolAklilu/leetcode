class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_xor = []
        for i in range(len(arr)):
            if i == 0:
                pre_xor.append(arr[i])
            else:
                pre_xor.append(arr[i] ^ pre_xor[i-1])           
        
        res = [0] * len(queries)
        for i in range(len(queries)):
            left = queries[i][0]
            right  = queries[i][1]
            
            if left == 0:
                res[i] = pre_xor[right]
            else:
                res[i] = pre_xor[right] ^ pre_xor[left-1]
                
        return res
    
