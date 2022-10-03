class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right, left_sum, right_sum = 0, len(cardPoints) - 1, 0, 0
        right_s, left_s = [0], [0]
        
        while left <= len(cardPoints) - 1 and right >= 0:
            left_sum += cardPoints[left]
            right_sum += cardPoints[right]
            
            right_s.append(right_sum)
            left_s.append(left_sum)
            
            left += 1
            right -= 1
        
        all_score = []
        for i in range(k+1):
            all_score.append(left_s[i] + right_s[k-i])
            
        return max(all_score)
        
