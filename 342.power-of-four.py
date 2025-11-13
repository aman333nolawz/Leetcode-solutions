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
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        q, r = divmod(n, 4)
        while 1:
            if r != 0:
                if q == 0 and r == 1:
                    return True
                return False

            if (q, r) == (1, 0):
                return True
            q, r = divmod(q / 4, 4)
        return True


# @leet end

