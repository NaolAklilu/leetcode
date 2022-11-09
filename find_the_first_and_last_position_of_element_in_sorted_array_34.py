class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        count = nums.count(target)
        
        idx = nums.index(target)
        
        return [idx, idx+count-1]
