class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rangeList = []
        for i in range(len(nums) + 1):
            rangeList.append(i)
        
        for i in range(len(nums)):
            rangeList.remove(nums[i])
            
        return rangeList[0]
