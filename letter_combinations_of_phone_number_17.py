class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":["a", "b","c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k","l"],
              "6":["m","n","o"], "7":["p","q","r","s"], "8":["t", "u", "v"], "9":["w","x", "y", "z"]}
        
        if digits == "":
            return []
        
        if len(digits) == 1:
            return dic[digits]
        
        elif len(digits) == 2:
            res = []
            for char1 in dic[digits[0]]:
                for char2 in dic[digits[1]]:
                    res.append(char1+char2)
            return res
        
        elif len(digits) == 3:
            res = []
            for char1 in dic[digits[0]]:
                for char2 in dic[digits[1]]:
                    for char3 in dic[digits[2]]:
                        res.append(char1+char2+char3)
            return res
        
        elif len(digits) == 4:
            res = []
            for char1 in dic[digits[0]]:
                for char2 in dic[digits[1]]:
                    for char3 in dic[digits[2]]:
                        for char4 in dic[digits[3]]:
                            res.append(char1+char2+char3+char4)
            return res
                
                
