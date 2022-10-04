class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        left, right = 1 , len(nums) - 1
        left_mult, right_mult = 1, 1
        while left <= len(nums) - 1:
            ans[left] = ans[left - 1] * nums[left - 1]
            left += 1
            
        while right >= 0:
            ans[right] *= right_mult
            right_mult *= nums[right]
            right -= 1
            
        return ans
