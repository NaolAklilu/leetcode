class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:       
        nums = sorted(nums)
        array = []
        i = 0
        j = len(nums) - 1
        
        while len(array) < len(nums):
            array.append(nums[i])
            i += 1
            if i <= j:
                array.append(nums[j])
                j -= 1

        return(array)
