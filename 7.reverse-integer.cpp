// @leet start
#include <cmath>
#include <cstdint>
class Solution {
public:
  int reverse(int x) {
    uint64_t out = 0;
    bool negative = false;

    if (x <= -pow(2, 31))
      return 0;

    if (x < 0) {
      x = -x;
      negative = true;
    }

    while (x > 0) {
      int digit = x % 10;
      out = out * 10 + digit;
      if (out >= std::pow(2, 31)) {
        return 0;
      }
      x /= 10;
    }
    return negative ? -out : out;
  }
};
// @leet end
