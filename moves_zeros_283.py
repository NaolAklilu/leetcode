class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        begin, end = 0, len(nums) - 1
        
        while begin < end:
            if nums[begin] == 0:
                end -= 1
                nums.remove(nums[begin])
                nums.append(0)
            else:
                 begin += 1
                
        return nums
