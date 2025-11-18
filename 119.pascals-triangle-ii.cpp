// @leet start
#include <cstdint>
#include <vector>
class Solution {
public:
  uint64_t c(uint64_t n, uint64_t r) {
    if (n - r > r) {
      r = n - r;
    }

    uint64_t out = 1;
    for (uint64_t i = n; i > r; i--) {
      out *= i;
    }

    for (uint64_t i = 1; i <= n - r; i++) {
      out /= i;
    }
    return out;
  }

  std::vector<int> getRow(int rowIndex) {
    std::vector<int> row;
    for (int i = 0; i <= rowIndex; i++) {
      row.push_back(c(rowIndex, i));
    }
    return row;
  }
};
// @leet end
