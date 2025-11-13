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
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        offset = 0
        while i1 < m + n:
            num1 = nums1[i1]
            num2 = nums2[i2] if i2 < n else float("inf")

            if nums1[m + offset - 1] <= num1 and nums1[m + offset - 1] != 0:
                nums1[i1] = nums1[m + offset]
                nums1[m + offset - 1] = num1

            if num1 == 0:
                nums1[i1] = num2
                i1 += 1
                i2 += 1
            else:
                if num1 <= num2:
                    i1 += 1
                else:
                    nums1[i1] = num2
                    nums1[m + offset] = num1
                    i1 += 1
                    i2 += 1
                    offset += 1


# @leet end

