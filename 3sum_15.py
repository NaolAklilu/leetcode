class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for first in range(len(nums)-2):
            second, third = first + 1, len(nums)-1  
            while second < third:
                sum = nums[first] + nums[second] + nums[third]                   
                if sum == 0:
                    res.add((nums[first], nums[second], nums[third]))
                    third -= 1
                    second += 1
                    
                elif sum < 0:
                    second += 1
                    
                else:
                    third -= 1
            
        return res
