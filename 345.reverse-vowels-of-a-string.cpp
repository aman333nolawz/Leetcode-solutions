// @leet start
#include <cctype>
#include <string>
class Solution {
public:
  std::string reverseVowels(std::string s) {
    std::string vowels = "";
    for (char c : s) {
      char lower = tolower(c);
      if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
        vowels += c;
      }
    }

    int vowelIndex = vowels.length() - 1;
    for (int i = 0; i < s.length(); i++) {
      char c = tolower(s[i]);
      if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
        s[i] = vowels[vowelIndex];
        vowelIndex--;
      }
    }
    return s;
  }
};
// @leet end
