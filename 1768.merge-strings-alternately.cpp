// @leet start
#include <algorithm>
#include <string>
class Solution {
public:
  std::string mergeAlternately(std::string word1, std::string word2) {
    int len1 = word1.length();
    int len2 = word2.length();
    std::string output = "";
    for (int i = 0; i < std::max(len1, len2); i++) {
      if (i < len1)
        output += word1[i];
      if (i < len2)
        output += word2[i];
    }
    return output;
  }
};
// @leet end
