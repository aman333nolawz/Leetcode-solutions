#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, a: int) -> int:
        x = 10**-3
        for _ in range(29):
            x -= x/2 - a/(2*x)
        return int(x)
# @lc code=end

