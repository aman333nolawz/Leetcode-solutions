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
    def numWaterBottles(self, numBottles: int, numExchange: int, numEmpty=0) -> int:
        if numBottles + numEmpty < numExchange:
            return numBottles
        return numBottles + self.numWaterBottles(
            (numBottles + numEmpty) // numExchange,
            numExchange,
            (numBottles + numEmpty) % numExchange,
        )


# @leet end

