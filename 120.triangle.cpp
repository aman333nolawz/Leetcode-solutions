// @leet start
class Solution {
public:
  int minimumTotal(vector<vector<int>> &triangle) {
    int result = 0;
    for (int i = 0; i < triangle.size(); i++) {
      int minimum = triangle[i][0];
      for (int j = 1; j < triangle[i].size(); j++) {
        if (triangle[i][j] < minimum)
          minimum = triangle[i][j];
      }
      result += minimum;
    }
    return result;
  }
};
// @leet end
