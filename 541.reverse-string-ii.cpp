// @leet start
#include <string>
class Solution {
public:
  std::string reverseStr(std::string s, int k) {
    int cur = 0;
    while (cur < s.size()) {
      if (cur + k > s.size()) {
        k = s.size() - cur;
      }
      for (int i = 0; i < k / 2; i++) {
        s[cur + i] ^= s[(cur + k) - i - 1];
        s[(cur + k) - i - 1] ^= s[cur + i];
        s[cur + i] ^= s[(cur + k) - i - 1];
      }
      cur += 2 * k;
    }
    return s;
  }
};
// @leet end
