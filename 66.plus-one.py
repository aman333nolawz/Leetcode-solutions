#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.add(digits, len(digits)-1)

    def add(self, digits, place):
        if place < 0: return digits
        if digits[place] == 9:
            digits[place] = 0
            if place == 0:
                digits.insert(0, 1)
            return self.add(digits, place-1)
        digits[place] += 1
        return digits
# @lc code=end

