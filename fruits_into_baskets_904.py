class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right, max_value = 0, 0, 0
        dic = {}

        if len(fruits) <= 2:
            return  len(fruits)
        
        while right <= len(fruits) - 1:
            if fruits[right] not in dic.keys():
                dic[fruits[right]] = 1
            else:
                dic[fruits[right]] += 1 
                
            while len(dic) > 2:
                dic[fruits[left]] -= 1
                if dic[fruits[left]] == 0:
                    dic.pop(fruits[left])
                
                left += 1
                
            max_value = max(max_value, sum(dic.values()))
            right += 1
            
        return max_value
