class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right, maxScore = 0, 0, 0
        total_sum = sum(cardPoints)
        
        if len(cardPoints) == k:
            return total_sum
        
        cur_sum = 0
        while right <= len(cardPoints) - 1:
            while (right - left + 1) <= len(cardPoints) - k:
                cur_sum += cardPoints[right]
                right += 1
                
            maxScore = max(maxScore, (total_sum - cur_sum))
            cur_sum -= cardPoints[left]
            left += 1
            
        return maxScore
    
        
