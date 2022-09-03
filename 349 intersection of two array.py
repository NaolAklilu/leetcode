class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_list = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    if i not in intersection_list:
                        intersection_list.append(i)
                        
                        
        return intersection_list
