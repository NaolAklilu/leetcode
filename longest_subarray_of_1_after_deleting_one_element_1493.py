class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        left, right = 0, 0
        
        max_arr = 0
        
        while right <= len(nums) - 1:
            
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            if max_arr < (right - left):
                max_arr = (right - left)
            
            right += 1     
            
        return max_arr
                           
