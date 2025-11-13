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
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        for i in range(1 << n):
            subset = [nums[j] for j in range(n) if i & (1 << j)]
            if sum(subset) == k:
                print(subset)
                total += 1
        return total


# @leet end
