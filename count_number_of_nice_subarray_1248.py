class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odd_count, current_nice, all_nice = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
                
        for num in nums:
            if num == 1:
                odd_count += 1
                current_nice = 0
                
            while odd_count == k:
                if nums[left] == 1:
                    odd_count -= 1
                    
                left += 1
                current_nice += 1
                
            all_nice += current_nice

        return all_nice
                    
                
    
