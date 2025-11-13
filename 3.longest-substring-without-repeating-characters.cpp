// @leet start
#include <string>

class Solution {
public:
  int lengthOfLongestSubstring(std::string s) {
    int left = 0;
    int lenOfLongestSubstr = 0;
    std::string subStr = "";
    int subStrStart = 0;

    while (left < s.length()) {
      for (int i = 0; i < subStr.length(); i++) {
        if (s[left] == subStr[i]) {
          subStr = "";
          subStrStart++;
          left = subStrStart;
          break;
        }
      }

      subStr += s[left];
      left++;

      if (subStr.length() > lenOfLongestSubstr) {
        lenOfLongestSubstr = subStr.length();
      }
    }

    return lenOfLongestSubstr;
  }
};
// @leet end
