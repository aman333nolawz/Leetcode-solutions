// @leet start
#include <vector>
class Solution {
public:
  std::vector<int> dailyTemperatures(std::vector<int> &temperatures) {
    std::vector<int> out;
    out.reserve(temperatures.size());

    for (int i = 0; i < temperatures.size(); i++) {
      if (i == temperatures.size() - 1) {
        out.push_back(0);
        return out;
      }

      for (int j = i + 1; j < temperatures.size(); j++) {
        if (temperatures[j] > temperatures[i]) {
          out.push_back(j - i);
          break;
        }
      }
      if (out.size() - 1 != i) {
        out.push_back(0);
      }
    }
    return out;
  }
};
// @leet end
