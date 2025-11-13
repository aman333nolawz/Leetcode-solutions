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
    def firstMissingPositive(self, nums: List[int]) -> int:
        out = [0] * (len(nums) + 1)
        for num in nums:
            if 0 <= num - 1 < len(nums):
                out[num - 1] = 1
        return out.index(0) + 1


# @leet end
