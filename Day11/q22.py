"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
day11pt1.py (c) 2024
Desc: description
Created:  2024-12-11T04:12:12.495Z
Modified: 2024-12-11T07:45:48.394Z
"""

from tqdm import tqdm
from functools import lru_cache
from time import time

with open("input.txt", "r") as f:
    arr = list(map(int, f.readlines()[0].strip().split()))


@lru_cache(maxsize=None)
def recur(n, num_iter=0):
    if num_iter == 75:
        return 1

    if n == 0:
        return recur(1, num_iter + 1)

    str_n = str(n)
    if len(str_n) % 2 == 0:
        return recur(int(str_n[: len(str_n) // 2]), num_iter + 1) + recur(int(str_n[len(str_n) // 2 :]), num_iter + 1)

    return recur(2024 * n, num_iter + 1)


t0 = time()
ans = 0
for x in arr:
    ans += recur(x)
print(ans)
print("Time taken:", time() - t0)
