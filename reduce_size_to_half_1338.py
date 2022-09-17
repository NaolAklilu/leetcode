class Solution(object):
    def minSetSize(self, arr):
        nums = set()
        num_freq = []
        
        half = len(arr) // 2
        
        num_dic = Counter(arr)
        
        for num in list(num_dic.items()):
            num_freq.append(list(num))
        
        num_freq.sort(key=lambda num:num[1], reverse=True)
        
        count = 0
        sum = 0
        for num in num_freq:
            count += 1
            sum += num[1]
            if sum >= half:
                return count
