// @leet start
class Solution {
public:
  void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    int l = 0;
    int r = 0;

    while (r != n) {
      if (nums1[l] > nums2[r]) {
        nums1[l] ^= nums2[r];
        nums2[r] ^= nums1[l];
        nums1[l] ^= nums2[r];
        l += 1;
      } else if (nums1[l] == 0) {
        nums1[l] ^= nums2[r];
        nums2[r] ^= nums1[l];
        nums1[l] ^= nums2[r];
        r += 1;
        l += 1;
      } else {
        l += 1;
      }
    }
  }
};
// @leet end
