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
    def solveNQueens(self, n: int) -> List[List[str]]:
        solns = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        negDiag = set()
        posDiag = set()

        def solve(r):
            if r == n:
                solns.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or r + c in posDiag or r - c in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                solve(r + 1)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        solve(0)
        return solns


# @leet end
