class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicatedNums = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                duplicatedNums.append(idx + 1)
            else:
                nums[idx] = -(nums[idx])
                
        return duplicatedNums
