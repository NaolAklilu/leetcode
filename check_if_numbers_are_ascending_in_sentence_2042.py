class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = list(s.split(" "))
        nums = []
        for i in range(len(s)):
            if s[i].isnumeric():
                if len(nums) == 0:
                    nums.append(s[i])
                else:
                    if int(s[i]) <= int(nums[-1]):
                        return False
                    else:
                        nums.append(s[i])
 
        return True
                
