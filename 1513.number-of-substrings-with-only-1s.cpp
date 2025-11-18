// @leet start
#include <cstdint>
class Solution {
public:
  int numSub(string s) {
    uint64_t continous_ones = 0;
    uint64_t result = 0;
    for (char num : s) {
      if (num == '0') {
        result += ((continous_ones * (continous_ones + 1)) / 2) % (1000000007);
        continous_ones = 0;
      } else {
        continous_ones += 1;
      }
    }
    result += ((continous_ones * (continous_ones + 1)) / 2) % (1000000007);
    return result;
  }
};
// @leet end
