class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dic = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        
        max_vowel = sum(dic.values())
        left, right = 0, 0
        
        while right <= len(s) - 1:
            while (right - left + 1) <= k:
                if s[right] in dic.keys():
                    dic[s[right]] += 1
                
                right += 1
            
            if max_vowel < sum(dic.values()):
                max_vowel = sum(dic.values())
                
            if s[left] in dic.keys():
                dic[s[left]] -= 1
            left += 1
            
        return max_vowel
            
                
