// @leet start
class Solution {
public:
  long long flowerGame(int n, int m) {
    unsigned long long x_odd = n / 2;
    unsigned long long x_even = n - x_odd;
    unsigned long long y_odd = m / 2;
    unsigned long long y_even = m - y_odd;
    return x_odd * y_even + x_even * y_odd;
  }
};
// @leet end
