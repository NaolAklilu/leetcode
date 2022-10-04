class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        good_days = []
        good_days_count = 0
        
        decreasing = [0] * len(security)
        for i in range(1, len(security)):
            good_days_count =  (good_days_count + 1) if security[i] <= security[i-1] else 0
            decreasing[i] = good_days_count
        
        good_days_count = 0
        increasing = [0] * len(security)
        for i in range(len(security) - 2, -1, -1):
            good_days_count =  (good_days_count + 1) if security[i] <= security[i+1] else 0  
            increasing[i] = good_days_count
            
        for i in range(len(security)):
            if decreasing[i] >= time and increasing[i] >= time:
                good_days.append(i)
        
        return good_days
