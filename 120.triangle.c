// @leet start
#include <stdio.h>
#include <string.h>

int minimumTotal(int **triangle, int triangleSize, int *triangleColSize) {
  int dp[triangleColSize[triangleSize - 1] + 1];
  memset(dp, 0, (triangleColSize[triangleSize - 1] + 1) * sizeof(int));

  for (int i = triangleSize - 1; i >= 0; i--) {
    int *row = triangle[i];
    for (int j = 0; j < triangleColSize[i]; j++) {
      int n1 = dp[j];
      int n2 = dp[j + 1];
      dp[j] = row[j] + (n1 < n2 ? n1 : n2);
    }
  }
  return dp[0];
}
// @leet end
