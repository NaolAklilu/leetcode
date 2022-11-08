class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        for i in range(len(nums)):
            if nums[i] == val:
                nums.remove(nums[i])
                nums.append(val)
        
        
        for i in range(count):
            nums.pop()
                
        
