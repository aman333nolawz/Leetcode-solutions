#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        sum = 0
        while sum < dividend:
            sum += divisor
            count += 1
        return count

# @lc code=end

