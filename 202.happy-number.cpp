// @leet start
#include <cmath>
class Solution {
public:
  bool isHappy(int n) {
    while (1) {
      int square_sum = 0;
      while (n != 0) {
        square_sum += std::pow(n % 10, 2);
        n /= 10;
      }

      if (square_sum == 1)
        return true;
      else if (square_sum == 4)
        return false;

      n = square_sum;
    }
  }
};
// @leet end
