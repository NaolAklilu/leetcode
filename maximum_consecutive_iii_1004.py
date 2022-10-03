class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, zeros = 0, 0, 0
        current_window_size, max_window_size = 0, 0
        
        while right <= len(nums) - 1 and left <= len(nums) - 1:
            if nums[right] == 0:
                zeros += 1
                
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1 
                left += 1
                current_window_size -= 1
                
            right += 1
            current_window_size += 1
                
            if current_window_size > max_window_size:
                max_window_size = current_window_size
                    
        return max_window_size
            
            
