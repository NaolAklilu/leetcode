class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        decent_period = [1] * len(prices)
        
        total_dPeriod = 1
        if len(prices) == 1:
            return 1
        
        for i in range(1, len(prices)):
            if prices[i-1] - prices[i] == 1:
                decent_period[i] = decent_period[i-1] + 1
            
            total_dPeriod += decent_period[i] 
        
        return  total_dPeriod
