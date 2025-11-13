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
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = 0
        while i <= len(nums) - 3:
            if nums[i] < nums[i + 1] < nums[i + 2]:
                return True
            i += 1

        return False


# @leet end

