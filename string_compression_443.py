class Solution:
    def compress(self, chars: List[str]) -> int:
        begin, end = 0, 1
        
        s = []
        length = len(chars) - 1
        if len(chars) == 1:
            return 1
        
        while end <= len(chars) - 1:
            if end == len(chars) - 1 and chars[begin] == chars[end]:
                s.append(chars[begin])
                if chars[begin] != chars[end]:
                    s.append(chars[end])
                elif end - begin + 1 >= 10:
                    for char in str(end - begin + 1):
                        s.append(char)
                elif 1 < end - begin + 1 < 10:
                    s.append(str(end - begin + 1))
                begin = end
                end += 1
                
            elif chars[begin] == chars[end]:
                end += 1
            elif chars[begin] != chars[end]:
                s.append(chars[begin])
                if end - begin >= 10:
                    for char in str(end - begin):
                        s.append(char)
                elif 1 < (end - begin) < 10:
                    s.append(str(end - begin))
                begin = end
                # end += 1
        
        del chars[:]
        chars.extend(s)
        
        return len(s) 
      
      
