// @leet start
#include <string>
class Solution {
public:
  int maxOperations(std::string s) {
    int res = 0;
    int one_count = 0;
    bool encountered_one = false;

    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '1') {
        encountered_one = true;
        one_count += 1;
      } else if (encountered_one) {
        res += one_count;
        encountered_one = false;
      }
    }
    return res;
  }
};
// @leet end
