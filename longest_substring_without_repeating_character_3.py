class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest_str = 0
        new_str = ""
        
        if len(s) == 1:
            return 1
        
        while right <= len(s) - 1:
            if s[right] in new_str:
                while s[right] in new_str:
                    new_str = new_str[1:]
                    
            new_str += s[right]
            longest_str = max(longest_str, len(new_str))
            right += 1
            
        return longest_str   
