class Solution:
    def partitionString(self, s: str) -> int:
        temp = ''
        count = 0
        for char in s:
            if char in temp:
                count += 1
                temp = ''
            temp = "".join((temp, char))
        
        if temp == "":
            return count
        else:
            return count + 1
