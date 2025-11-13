// @leet start
#include <numeric>
#include <string>
class Solution {
public:
  std::string gcdOfStrings(std::string str1, std::string str2) {
    int max, min;
    int len1 = str1.length();
    int len2 = str2.length();

    int gcd = std::gcd(len1, len2);
    std::string gcdStr = "";

    for (int i = 0; i < gcd; i++) {
      if (str1[i] != str2[i])
        return "";
      gcdStr += str1[i];
    }

    for (int i = 0; i < len1; i++) {
      if (str1[i] != gcdStr[i % gcd])
        return "";
    }
    for (int i = 0; i < len2; i++) {
      if (str2[i] != gcdStr[i % gcd])
        return "";
    }

    return gcdStr;
  }
};
// @leet end
