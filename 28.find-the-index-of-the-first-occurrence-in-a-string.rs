/*
 * @lc app=leetcode id=28 lang=rust
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if haystack.len() < needle.len() {
            return -1;
        }
        for i in 0..(haystack.len() - needle.len() + 1) {
            if haystack[i..i + needle.len()] == needle {
                return i as i32;
            }
        }
        return -1;
    }
}
// @lc code=end
