class Solution:
    def pivotIndex(self, nums: List[int]) -> int: 
        left_sum = 0
        right_sum = 0
        
        total_sum = sum(nums)
            
        for i in range(0, len(nums)):
            if i == 0:
                left_sum = 0
                right_sum = total_sum - left_sum - nums[i]
            elif i == len(nums) - 1:
                right_sum = 0
                left_sum += nums[i-1]
            else:
                left_sum += nums[i-1]
                right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
        
        return -1
