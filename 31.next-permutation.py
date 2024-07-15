#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0


    def get_(self, nums, n):
        left = 0
        right = len(nums) - 1
        order = len(nums) - 1

        while left < right:
            n += nums[left] * 10**(order-left)

# @lc code=end

