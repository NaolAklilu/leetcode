class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        first = 0
        while first in range(len(nums)-2):
            second = first + 1
            while second in range(len(nums)-1):
                third = second + 1
                if nums[second] - nums[first] == diff:
                    while third in range(len(nums)):
                        if nums[third] - nums[second] == diff:
                            count += 1
                            third += 1
                        else:
                            third += 1
                    second += 1
                else:
                    second += 1
            first += 1
                    
        return count

                
            
            
