// @leet start
#include <string>
#include <vector>

class Solution {
public:
  std::string reverseWords(std::string s) {
    std::vector<std::string> words;
    std::string word = "";
    for (char c : s) {
      if (c == ' ') {
        if (word == "")
          continue;
        words.push_back(word);
        word = "";
        continue;
      }
      word += c;
    }

    if (word != "")
      words.push_back(word);

    s = "";
    for (int i = words.size() - 1; i >= 0; i--) {
      s.append(words[i]);
      if (i != 0)
        s += ' ';
    }

    return s;
  }
};
// @leet end
