class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        left = len(nums) - 2
        while left != -1:
            if nums[left] < nums[left+1]:
                break
                
            left -= 1
        
        if left < 0:
            nums.reverse()
        else:
            right = len(nums) - 1
            while left < right:
                if nums[right] > nums[left]:
                    break
                right -= 1
            
            nums[right], nums[left] = nums[left], nums[right]
            nums[left+1:] = nums[left+1:][::-1]
            
        return nums
