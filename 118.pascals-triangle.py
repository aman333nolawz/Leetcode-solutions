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
    def c(self, n, r):
        return self.fact(n) // (self.fact(r) * self.fact(n - r))

    def fact(self, n, memo={}):
        if n == 0:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = n * self.fact(n - 1, memo)
        return memo[n]

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for y in range(1, numRows):
            row = []
            for x in range(y + 1):
                row.append(self.c(y, x))
            triangle.append(row)
        return triangle


# @leet end

