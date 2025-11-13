// @leet start
#include <cstdlib>
#include <vector>
class Solution {
public:
  int firstMissingPositive(std::vector<int> &nums) {
    bool *arr = (bool *)calloc(nums.size() + 1, sizeof(bool));

    for (int i = 0; i < nums.size(); i++) {
      int num = nums[i];
      if (1 <= num and nums.size() + 1 > num) {
        arr[num - 1] = true;
      }
    }

    for (int i = 0; i < nums.size() + 1; i++) {
      if (!arr[i]) {
        return i + 1;
      }
    }
    return nums.size() + 1;
  }
};
// @leet end
