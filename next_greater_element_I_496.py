class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        result = []
        for num in nums1:
            stack = []
            for number in nums2:
                stack.append(number)
                
            greater_num = -1
            while stack[-1] != num:
                stack_top = stack.pop()
                if stack_top > num:
                    greater_num = stack_top
            result.append(greater_num)
        
        return result
