class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_num = []
        odd_num = []
        
        for i in nums:
            if i % 2 == 0:
                even_num.append(i)
            elif i % 2 != 0:
                odd_num.append(i)
        
        result = []  
        for i in range(0, len(nums)):
            if i % 2 == 0:
                result.append(even_num[0])
                even_num.remove(even_num[0])
            elif i % 2 != 0:
                result.append(odd_num[0])
                odd_num.remove(odd_num[0])
        
        return result
