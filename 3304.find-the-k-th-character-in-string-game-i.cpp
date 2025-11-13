// @leet start
#include <string>
class Solution {
public:
  char kthCharacter(int k) {
    std::string s = "a";
    while (s.length() < k) {
      for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if (c == 'z')
          s += 'a';
        else
          s += c + 1;
      }
    }
    return s[k - 1];
  }
};
// @leet end
