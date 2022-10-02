class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        end = 1
        while end <= k:
            last_element = nums.pop()
            nums.insert(0, last_element)
            
            end += 1
            
        return nums
        
