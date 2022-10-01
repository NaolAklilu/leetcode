class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        begin = 0
        end = 1
        
        result = set()
        
        nums.sort()
        
        if len(nums) == 1:
            return 0
        
        while end <= len(nums) - 1 and begin <= len(nums) - 2:
            if (nums[end] - nums[begin]) == k:
                result.add(tuple([nums[begin], nums[end]]))
                begin += 1
                end += 1
            elif (nums[end] - nums[begin]) > k:
                begin += 1
                if begin == end:
                    end += 1
            elif (nums[end] - nums[begin]) < k:
                end += 1
        
        return len(result)
