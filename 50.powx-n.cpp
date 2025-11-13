// @leet start
#include <cstdint>
class Solution {
public:
  double myPow(double x, int n) {
    uint64_t power = n;
    if (x == 0)
      return 0;
    if (x == 1)
      return 1;
    if (n == 0)
      return 1;

    if (n < 0) {
      x = 1 / x;
      power = -n;
    }

    double result = x;

    for (int _ = 0; _ < power / 2; _++) {
      result *= result;
    }
    return result;
  }
};
// @leet end
