class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score, left, right = 0, 0, len(tokens) - 1
        
        while left < right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
            elif score >= 1 and power >= tokens[left] - tokens[right]:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
                
        if left == right and power >= tokens[left]:
            power -= tokens[left]
            score += 1
            
        
        return score
