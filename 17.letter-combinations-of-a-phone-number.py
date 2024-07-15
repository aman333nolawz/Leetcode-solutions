#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out = []
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, string):
            if len(string) == len(digits):
                out.append(string)
                return
            for char in digit_to_letter[digits[i]]:
                backtrack(i + 1, string + char)

        if digits:
            backtrack(0, "")
        return out
      
# @lc code=end

