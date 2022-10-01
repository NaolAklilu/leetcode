class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_array_length = len(nums) + 1
        begin = 0
        end = 0
        
        sum = 0
        while end <= len(nums) - 1:
            sum += nums[end]
            if sum >= target:                                
                while sum >= target:
                    if min_array_length > (end - begin + 1):
                        min_array_length = (end - begin + 1)
                    sum -= nums[begin]
                    begin += 1
                    
            end += 1
        
        return min_array_length if min_array_length != len(nums)+1 else 0                    
