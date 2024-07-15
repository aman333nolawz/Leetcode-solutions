#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            midpoint = left + (right-left) // 2
            if nums[midpoint] == target: return midpoint
            if target > nums[midpoint]:
                left = midpoint + 1
            elif target < nums[midpoint]:
                right = midpoint - 1

        return left
        
# @lc code=end

