// @leet start
#include <iostream>
#include <string>
class Solution {
public:
  bool isPalindrome(std::string s) {
    int left = 0;
    int right = s.length();

    while (left < right) {
      char leftChar = s[left];
      char rightChar = s[right];

      if (leftChar >= 65 && leftChar <= 90) {
        leftChar = leftChar + 32;
      }

      if (!(leftChar >= 97 && leftChar <= 122) &&
          !(leftChar >= 48 && leftChar <= 57)) {
        left++;
        continue;
      }

      if (rightChar >= 65 && rightChar <= 90) {
        rightChar = rightChar + 32;
      }

      if (!(rightChar >= 97 && rightChar <= 122) &&
          !(rightChar >= 48 && rightChar <= 57)) {
        right--;
        continue;
      }

      if (leftChar != rightChar)
        return false;

      left++;
      right--;
    }
    return true;
  }
};
// @leet end
