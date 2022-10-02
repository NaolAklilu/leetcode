class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        begin, end = 0, len(nums) - 1
        res = [0]*len(nums)

        while begin <= end:
            if abs(end) > abs(begin):
                res[end] = nums[end] ** 2
                end -= 1
                
            else:
                res[begin] = nums[begin] ** 2
                begin += 1
        
        return sorted(res)
                
