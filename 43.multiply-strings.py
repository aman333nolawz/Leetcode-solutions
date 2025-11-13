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
    def toint(self, char: str) -> int:
        return ord(char) - ord("0")

    def multiply(self, num1: str, num2: str) -> str:
        result = "0" * (len(num1) + len(num2))
        for i, d1 in enumerate(num1):
            for j, d2 in enumerate(num2):
                mul = str(self.toint(d1) * self.toint(d2))

        return result


# @leet end

