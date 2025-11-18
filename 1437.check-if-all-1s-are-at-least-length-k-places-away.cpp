// @leet start
class Solution {
public:
  bool kLengthApart(vector<int> &nums, int k) {
    int dist = 0;
    bool started = false;

    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == 1) {
        if (started) {
          if (dist < k)
            return false;
        } else {
          started = true;
        }
        dist = 0;
      } else {
        dist += 1;
      }
    }
    return true;
  }
};
// @leet end
