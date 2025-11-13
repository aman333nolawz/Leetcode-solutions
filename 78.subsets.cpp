// @leet start
#include <vector>
class Solution {
public:
  std::vector<std::vector<int>> subsets(std::vector<int> &nums) {
    std::vector<std::vector<int>> power_set;
    for (int i = 0; i < 1 << nums.size(); i++) {
      std::vector<int> subset;

      for (int j = 0; j < nums.size(); j++) {
        if (i & (1 << j))
          subset.push_back(nums[j]);
      }

      power_set.push_back(subset);
    }
    return power_set;
  }
};
// @leet end
