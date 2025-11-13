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

from string import ascii_lowercase


class Solution:
    def next_char(self, char):
        if char == "z":
            return "a"
        return chr(ord(char) + 1)

    def kthCharacter(self, k: int, base=-1) -> str:
        if k == 1:
            return "a"
        if base == -1:
            base = int(log2(k))

        remainder = k % (1 << base)
        if remainder == 0:
            return ascii_lowercase[base]

        if remainder <= (1 << (base - 1)):
            return self.next_char(self.kthCharacter(remainder, int(log2(remainder))))

        return self.next_char(self.kthCharacter(remainder, base - 1))


# @leet end
