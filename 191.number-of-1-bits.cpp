// @leet start
class Solution {
public:
  int hammingWeight(int n) {
    int count;
    for (count = 0; n; count++) {
      n &= n - 1;
    }

    return count;
  }
};
// @leet end
