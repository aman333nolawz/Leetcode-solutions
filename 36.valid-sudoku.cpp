// @leet start
#include <vector>
class Solution {
public:
  bool isValidCell(std::vector<std::vector<char>> &board, int x, int y) {
    int num = board[y][x];
    for (int i = 0; i < 9; i++) {
      if (board[y][i] == num && i != x) {
        return false;
      }
      if (board[i][x] == num && i != y) {
        return false;
      }
    }

    int box_x = (x / 3) * 3;
    int box_y = (y / 3) * 3;

    for (int i = box_x; i < box_x + 3; i++) {
      for (int j = box_y; j < box_y + 3; j++) {
        if (i == x && j == y)
          continue;
        if (board[j][i] == num)
          return false;
      }
    }

    return true;
  }

  bool isValidSudoku(std::vector<std::vector<char>> &board) {
    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        if (board[j][i] == '.')
          continue;
        if (!isValidCell(board, i, j))
          return false;
      }
    }
    return true;
  }
};
// @leet end
