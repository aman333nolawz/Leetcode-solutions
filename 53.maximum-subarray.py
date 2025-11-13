# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
from typing import *
# @leet imports end


# @leet start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        n = len(nums)
        l = r = (1 << n) - 1
        while l != 0 and r != 0:
            left = [nums[j] for j in range(n) if l & (1 << j)]
            right = [nums[j] for j in range(n) if r & (1 << j)]
            if sum(left) > max_sum:
                max_sum = sum(left)
            if sum(right) > max_sum:
                max_sum = sum(right)

            print(left, right)

            l = (l << 1) & ((1 << n) - 1)
            r >>= 1

        return max_sum


# @leet end
