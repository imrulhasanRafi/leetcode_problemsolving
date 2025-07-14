class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []   
        digit_to_chars = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }       
        res = []      
        def backtrack(index=0, path=""):
            if index == len(digits):
                res.append(path)
                return           
            for char in digit_to_chars[digits[index]]:
                backtrack(index + 1, path + char)      
        backtrack()
        return res
