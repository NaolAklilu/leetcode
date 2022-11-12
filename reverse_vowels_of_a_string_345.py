class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)           
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']
        left, right = 0 , len(string)-1
        while left < right:
            if string[left] in vowels and string[right] in vowels:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
            
            elif string[left] in vowels and string[right] not in vowels:
                right -= 1
            
            elif string[left] not in vowels and string[right] in vowels:
                left += 1
                
            elif string[left] not in vowels and string[right] not in vowels:
                left += 1
                right -= 1
                
        return "".join(string)
