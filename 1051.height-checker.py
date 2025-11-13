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
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        mistakes = 0
        for ex, he in zip(expected, heights):
            if ex != he:
                mistakes += 1
        return mistakes


# @leet end

