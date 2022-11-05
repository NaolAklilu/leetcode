class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        prefix_sum_dic = {}
        prefix_sum_dic[sum] = 1
        
        for num in nums:
            sum += num
            pre_sum = sum - k
            
            if pre_sum in prefix_sum_dic.keys():
                count += prefix_sum_dic[pre_sum]
            
            if sum in prefix_sum_dic.keys():
                prefix_sum_dic[sum] += 1
            else:
                prefix_sum_dic[sum] = 1
        
        return count
