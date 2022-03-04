class Solution:
    def minPairSum(self, nums: List[int]) -> int:
    # def min_max_pair(arr):
        nums.sort()
        sum_arr = []
        for i in range(len(nums) // 2):
            sum_arr.append((nums[i] + nums[len(nums)-1-i]))

        sum_arr.sort()
        max_sum = sum_arr[-1] 
        
        return max_sum
