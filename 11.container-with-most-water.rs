/*
 * @lc app=leetcode id=11 lang=rust
 *
 * [11] Container With Most Water
 */

// @lc code=start
use std::cmp;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut max_area = 0;
        while left < right {
            let area = (right - left) as i32 * cmp::min(height[left], height[right]);
            max_area = cmp::max(area, max_area);
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return max_area;
    }
}

// @lc code=end
