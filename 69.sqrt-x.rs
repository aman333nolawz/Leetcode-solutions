/*
 * @lc app=leetcode id=69 lang=rust
 *
 * [69] Sqrt(x)
 */

// @lc code=start
impl Solution {
    pub fn my_sqrt(a: i32) -> i32 {
        let mut x = a as f64;
        for _ in 0..20 {
            x -= x/2.0-a as f64/(2.0*x);
        }
        
        return x as i32;
    }
}
// @lc code=end

