// @leet start
#include <vector>
class Solution {
public:
  int maxSubArray(vector<int> &nums) {
    int max_sum = nums[0];
    for (int i = 0; i < 1 << nums.size(); i++) {
      int sum = 0;
      for (int j = 0; j < nums.size(); j++) {
        if (((1 << i) - 1) & (1 << j))
          sum += nums[j];
      }
      if (sum > max_sum)
        max_sum = sum;
    }
    return max_sum;
  }
};
// @leet end
