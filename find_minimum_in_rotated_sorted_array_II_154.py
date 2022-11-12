class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for _ in range(len(nums)):
            if nums[0] < nums[-1]:
                return nums[0]
            nums.insert(0, nums.pop())
            
        return nums[0]
