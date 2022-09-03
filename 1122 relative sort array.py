class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result_arr = []
        distinct_elements = []
        
        for i in arr2:
            for j in arr1:
                if j == i:
                    result_arr.append(j)
                    
        for j in arr1:
            if j not in arr2:
                distinct_elements.append(j)
        
        sorted_arr = sorted(distinct_elements)
                    
        
        return result_arr + sorted_arr
