// @leet start
#include <vector>
class Solution {
public:
  std::vector<bool> kidsWithCandies(std::vector<int> &candies,
                                    int extraCandies) {
    std::vector<bool> result;
    result.reserve(candies.size());
    int max = candies[0];

    for (int i = 1; i < candies.size(); i++) {
      if (candies[i] > max)
        max = candies[i];
    }

    for (int i = 0; i < candies.size(); i++) {
      result.push_back(candies[i] + extraCandies - max >= 0);
    }

    return result;
  }
};
// @leet end
