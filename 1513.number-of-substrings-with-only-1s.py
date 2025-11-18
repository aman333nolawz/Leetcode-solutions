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
    def numSub(self, s: str) -> int:
        count = 0
        continous_ones = 0
        for num in s:
            if num == "0":
                count += (continous_ones * (continous_ones + 1)) // 2
                continous_ones = 0
            elif num == "1":
                continous_ones += 1

        count += (continous_ones * (continous_ones + 1)) // 2
        return count


# @leet end
