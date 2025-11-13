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
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        out = []
        for num in range(m + n - 1):
            looping_range = range(num + 1) if num & 1 else range(num, -1, -1)
            for y in looping_range:
                x = num - y
                if y >= m or x >= n:
                    continue
                out.append(mat[y][x])
        return out


# @leet end
