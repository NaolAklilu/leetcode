class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums.sort()
        
        for first in range(len(nums)-3):
            second = first + 1
            while second < len(nums) - 2:
                third, fourth = second + 1, len(nums)-1
                while third < fourth:
                    sum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if sum == target:
                        result.add((nums[first], nums[second], nums[third], nums[fourth]))
                        fourth -= 1
                        third += 1
                    
                    elif sum < target:
                        third += 1
                    
                    else:
                        fourth -= 1
                        
                second += 1
        
        return result
