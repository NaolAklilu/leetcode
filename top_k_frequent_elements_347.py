class Solution(object):
    def topKFrequent(self, nums, k):
        nums_dic = Counter(nums)
        
        sorted_num = []
        
        for num in list(nums_dic.items()):
            sorted_num.append(list(num))
        
        sorted_num.sort(key=lambda num:num[1], reverse=True)
        
        res = []
        for i in range(k):
            res.append(sorted_num[i][0])
        
        return res
