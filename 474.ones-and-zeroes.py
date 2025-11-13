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
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in memo:
                return memo[(i, m, n)]

            skipped = dfs(i + 1, m, n)
            z_count, o_count = strs[i].count("0"), strs[i].count("1")
            if z_count > m or o_count > n:
                memo[(i, m, n)] = skipped
                return skipped
            memo[(i, m, n)] = max(skipped, 1 + dfs(i + 1, m - z_count, n - o_count))
            return memo[(i, m, n)]

        return dfs(0, m, n)


# @leet end

