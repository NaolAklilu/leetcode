class Solution:
    def kthLargestNumber(self, arr: List[str], m: int) -> str:
        new_arr = []
        for num in arr:
            new_arr.append(int(num))
        new_arr.sort()
        new_arr.reverse()
        
        return str(new_arr[m-1])
