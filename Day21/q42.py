"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q41.py (c) 2024
Desc: description
Created:  2024-12-21T12:15:23.008Z
Modified: 2024-12-22T00:02:31.429Z
"""

from time import time
import re
from functools import lru_cache


def get_numeric_sequence(i, j, ch):
    # You are at i,j, you need the moves to get to ch
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+"""
    grid = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["-1", "0", "A"]]

    r, c = -1, -1
    # Find the ch's i,j
    for r1 in range(len(grid)):
        for c1 in range(len(grid[r])):
            if grid[r1][c1] == ch:
                r, c = r1, c1
                break
    if r == -1 or c == -1:
        print(f"r and c are -1, error in numeric sequence function. {i=},{j=},{ch=}")
    # else:
    #     print("r,c :", r, c)
    shortest_seqs = [
        # Vertical first
        # Horizontal first
    ]
    # Vertical first:
    ans = ""
    if i < r:
        ans += "v" * abs(i - r)
    if r < i:
        ans += "^" * abs(i - r)
    if j < c:
        ans += ">" * abs(j - c)
    if j > c:
        ans += "<" * abs(j - c)
    # Validate sequence and make sure it doesnt go past the blank space
    # Only way to hit the blank space is by going Down
    if not (j == 0 and r == 3):
        # Not crossing invalid point
        shortest_seqs.append(ans + "A")

    # Horizontal first:
    ans = ""
    if j < c:
        ans += ">" * abs(j - c)
    if j > c:
        ans += "<" * abs(j - c)
    if i < r:
        ans += "v" * abs(i - r)
    if r < i:
        ans += "^" * abs(i - r)
    # Validate sequence and make sure it doesnt go past the blank space
    # Only way to hit the blank space is by going Left
    if not (i == 3 and c == 0):
        shortest_seqs.append(ans + "A")

    return list(set(shortest_seqs)), r, c


def directional_sequence(i, j, ch):
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """
    grid = [["-1", "^", "A"], ["<", "v", ">"]]

    r, c = -1, -1
    # Find the ch's i,j
    for r1 in range(len(grid)):
        for c1 in range(len(grid[r])):
            if grid[r1][c1] == ch:
                r, c = r1, c1
                break
    if r == -1 or c == -1:
        print(f"r and c are -1, error in directional sequence function. {i=},{j=},{ch=}")
    # else:
    #     print("r,c :", r, c)
    shortest_seqs = [
        # Vertical first
        # Horizontal first
    ]
    # Vertical first:
    ans = ""
    if i < r:
        ans += "v" * abs(i - r)
    if r < i:
        ans += "^" * abs(i - r)
    if j < c:
        ans += ">" * abs(j - c)
    if j > c:
        ans += "<" * abs(j - c)
    # Validate sequence and make sure it doesnt go past the blank space
    # Only way to hit the blank space is by going Up
    if not (j == 0 and r == 0):
        # Not crossing invalid point
        shortest_seqs.append(ans + "A")

    # Horizontal first:
    ans = ""
    if j < c:
        ans += ">" * abs(j - c)
    if j > c:
        ans += "<" * abs(j - c)
    if i < r:
        ans += "v" * abs(i - r)
    if r < i:
        ans += "^" * abs(i - r)
    # Validate sequence and make sure it doesnt go past the blank space
    # Only way to hit the blank space is by going Left
    if not (i == 0 and c == 0):
        shortest_seqs.append(ans + "A")

    return list(set(shortest_seqs)), r, c


def shortest_paths_to_code(i, j, code, is_numeric=False):
    last_seqs = []
    for ch in code:
        # First call the sequence the last robot needs to use
        if is_numeric:
            shortest_sequences, i, j = get_numeric_sequence(i, j, ch)
        else:
            shortest_sequences, i, j = directional_sequence(i, j, ch)

        last_seqs.append(shortest_sequences)
    return last_seqs


# def get_directions(code):

#     ans_last_seqs = shortest_paths_to_code(3,2,code,is_numeric=True)

#     for robot in range(2):
#         temp_ans_last_seqs=[]
#         print('Robot:',robot, 'Number of ans_last_seqs:', len(ans_last_seqs))
#         for last_seq in ans_last_seqs:
#             temp = shortest_paths_to_code(0,2,last_seq,is_numeric=False)
#             temp_ans_last_seqs += temp
#         # print("Len temp_ans_last_seqs before:", len(temp_ans_last_seqs))
#         min_len_temp = len(min(temp_ans_last_seqs, key=len))
#         temp_ans_last_seqs = [x for x in temp_ans_last_seqs if len(x)==min_len_temp]
#         # print("Len temp_ans_last_seqs after:", len(temp_ans_last_seqs))
#         ans_last_seqs = temp_ans_last_seqs

#     return ans_last_seqs


@lru_cache(maxsize=None)
def min_cost(seq, depth):
    if depth == 0:
        return len(seq)

    subseqs = shortest_paths_to_code(0, 2, seq, is_numeric=False)
    #subseqs is a list of lists where subseqs[i] is a list of the valid shortest paths between the i-1 and ith characters
    #eg: if code was 297A then subseqs=[[shortest paths from A to 2],[shortest paths from 2 to 9],[shortest paths from 9 to 7],[shortest paths from 7 to A]]

    cost = 0
    for sseq in subseqs:
        #For each of the shortest paths from i-1 to i, find the minimum cost going through all 25 robots
        #Cache results across all pairs of paths (A-2,2-9,9-7,7-A) since its one function
        cost += min([min_cost(s, depth - 1) for s in sseq])
    return cost


def get_directions(code):
    keypad_sequences = shortest_paths_to_code(3, 2, code, is_numeric=True)
    print(keypad_sequences)
    ans = 0
    for seqs in keypad_sequences:
        ans += min([min_cost(seq, 25) for seq in seqs])
    return ans


t0 = time()
ans = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        code = line.strip()
        print(code)
        # Call function to get the length of directions
        shortest_directions = get_directions(code)

        # Calculate complexity
        ans += shortest_directions * int(re.findall(r"\d+", line)[0])
        print(f"{shortest_directions=}")
        print("int =", int(re.findall(r"\d+", line)[0]))
        print("-" * 100)

print(ans)
print("Time Taken:", time() - t0)
