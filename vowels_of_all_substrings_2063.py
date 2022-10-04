class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set("aeiou")
        total_vowels, left, length = 0, 0, len(word)
        
        while left <= len(word) - 1:
            if word[left] in vowels:
                total_vowels += (length - left) * (left + 1)
                left += 1
            else:
                left += 1
                
        return total_vowels
