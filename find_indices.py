class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index_array = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        for j in range(0, len(nums)):
            if nums[j] == target:
                index_array.append(j)
        return(index_array)
