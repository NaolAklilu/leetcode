class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right, res = 0, 0, []
        p = "".join(sorted(p))
        
        if len(p) > len(s):
            return []
        
        elif len(p) == len(s):
            temp = "".join(sorted(s))
            if temp == p:
                return [0]
            else:
                return []
        
        cur_str = ""
        while right <= len(s) - 1:
            while (right - left + 1) <= len(p):
                cur_str += s[right]
                right += 1
            
            temp = "".join(sorted(cur_str))
            if temp == p:
                res.append(left)
                
            cur_str = cur_str[1:]
            left += 1
        
        return res
            
