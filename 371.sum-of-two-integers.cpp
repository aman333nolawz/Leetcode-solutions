// @leet start
#include <iostream>
class Solution {
public:
  int getSum(int a, int b) {
    int carry = 0;
    int result = 0;

    for (int i = 0; i < 2; i++) {
      int unit_a = a & 1;
      int unit_b = b & 1;
      std::cout << carry << " " << unit_a << " " << unit_b << std::endl;
      if (carry ^ unit_a ^ unit_b == 0) {
        result <<= 1;

        if (carry | unit_a | unit_b == 1) {
          carry = 1;
        }
      } else {
        result = (result << 1) | 1;

        if (carry == unit_a and unit_a == unit_b) {
          carry = 1;
        }
      }
      a >>= 1;
      b >>= 1;
    }

    return result;
  }
};
// @leet end
