class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)
        
        res = []
        while left < len(haystack)-len(needle)+1:
            if haystack[left:left+right] == needle:
                res.append(left)
            left += 1
        
        return res[0] if len(res) != 0 else -1
