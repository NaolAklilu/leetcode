class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        
        left_pointer = 0
        right_pointer = len(height) - 1
           
        
        while left_pointer < right_pointer:
            area = (right_pointer - left_pointer) * min(height[right_pointer], height[left_pointer])
            
            if max_area < area:
                max_area = area
                
            if height[right_pointer] <= height[left_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
                
        return max_area
