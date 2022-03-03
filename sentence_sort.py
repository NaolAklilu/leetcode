class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")    
        array_len = len(words)

        num_word_pair = []
        for i in range(0, array_len):
            string = words[i]
            len_str = len(string)
            num = int(string[-1])
            word = string[0:len_str - 1]
            num_word_pair.append([num, word])

        num_word_pair.sort()
        sentence = ""
        for key in range(len(num_word_pair)) :
            sep = "" if (key == len(num_word_pair) - 1) else " "
            sentence += num_word_pair[key][1] + sep

        return sentence
