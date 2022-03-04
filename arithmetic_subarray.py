class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        is_arithmetic = False;
        for m in range(len(l)):  # 0, 1 , 2
            sub_arr = nums[l[m]: r[m] + 1]
            sub_arr.sort()

            dif = sub_arr[1] - sub_arr[0]
            for i in range(len(sub_arr)-1):
                j = i + 1
                if(sub_arr[j] - sub_arr[i]) == dif:
                    is_arithmetic = True
                else:
                    is_arithmetic = False
                    break
            ans.append(is_arithmetic)
        return ans

        
