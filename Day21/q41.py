"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q41.py (c) 2024
Desc: description
Created:  2024-12-21T12:15:23.008Z
Modified: 2024-12-21T15:12:13.471Z
"""

import re


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
        print("r and c are -1, error")
    # else:
    #     print("r,c :", r, c)
    shortest_seqs = [
        #Vertical first
        #Horizontal first
    ]
    #Vertical first:
    ans = ""
    if i < r:
        ans += "v" * abs(i - r)
    if r < i:
        ans += "^" * abs(i - r)
    if j < c:
        ans += ">" * abs(j - c)
    if j > c:
        ans += "<" * abs(j - c)
    #Validate sequence and make sure it doesnt go past the blank space
    #Only way to hit the blank space is by going Down
    if not( j==0 and r==3 ):
        # Not crossing invalid point
        shortest_seqs.append(ans+'A')

    #Horizontal first:
    ans = ""
    if j < c:
        ans += ">" * abs(j - c)
    if j > c:
        ans += "<" * abs(j - c)
    if i < r:
        ans += "v" * abs(i - r)
    if r < i:
        ans += "^" * abs(i - r)
    #Validate sequence and make sure it doesnt go past the blank space
    #Only way to hit the blank space is by going Left
    if not(i==3 and c==0):
        shortest_seqs.append(ans+'A')
    
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
        print("r and c are -1, error")
    # else:
    #     print("r,c :", r, c)
    shortest_seqs = [
        #Vertical first
        #Horizontal first
    ]
    #Vertical first:
    ans = ""
    if i < r:
        ans += "v" * abs(i - r)
    if r < i:
        ans += "^" * abs(i - r)
    if j < c:
        ans += ">" * abs(j - c)
    if j > c:
        ans += "<" * abs(j - c)
    #Validate sequence and make sure it doesnt go past the blank space
    #Only way to hit the blank space is by going Up
    if not( j==0 and r==0 ):
        # Not crossing invalid point
        shortest_seqs.append(ans+'A')

    #Horizontal first:
    ans = ""
    if j < c:
        ans += ">" * abs(j - c)
    if j > c:
        ans += "<" * abs(j - c)
    if i < r:
        ans += "v" * abs(i - r)
    if r < i:
        ans += "^" * abs(i - r)
    #Validate sequence and make sure it doesnt go past the blank space
    #Only way to hit the blank space is by going Left
    if not(i==0 and c==0):
        shortest_seqs.append(ans+'A')
    
    return list(set(shortest_seqs)), r, c



def shortest_paths_to_code(i,j,code,is_numeric=False):
    last_seqs = []
    for ch in code:
        # First call the sequence the last robot needs to use
        if is_numeric:
            shortest_sequences, i, j = get_numeric_sequence(i, j, ch)
        else:
            shortest_sequences, i, j = directional_sequence(i, j, ch)
        # print(ch,":",shortest_sequences)
        # print('last seq before adding:',last_seqs)
        if len(last_seqs) == 0:
            last_seqs = shortest_sequences
        else:
            temp_last_seqs = []
            for idx,seq in enumerate(last_seqs):
                for shortest_seq in shortest_sequences:
                    temp_last_seqs.append(seq + shortest_seq)
            last_seqs = temp_last_seqs
        # print('last seq after adding:',last_seqs)
    return list(set(last_seqs))



def get_directions(code):

    last_seqs = shortest_paths_to_code(3,2,code,is_numeric=True)
    
    # print("The last robot will input the sequence:", last_seqs)

    # Get the sequence the 2nd last robot will input to the last direction bot
    second_last_seqs=[]
    for last_seq in last_seqs:
        second_last_seqs += shortest_paths_to_code(0,2,last_seq,is_numeric=False)

    # print("The 2nd last robot will input the sequence:", second_last_seqs)

    # Get the sequnce you have to input to the first robot
    third_last_seqs=[]
    for last_seq in second_last_seqs:
        third_last_seqs += shortest_paths_to_code(0,2,last_seq,is_numeric=False)

    # print("The 3rd last robot will input the sequence:", third_last_seqs)
    return third_last_seqs


ans = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        code = line.strip()
        print(code)
        # Call function to get the directions
        directions = get_directions(code)
        shortest_directions = min(directions, key=len)
        # Calculate complexity
        ans += len(shortest_directions) * int(re.findall(r"\d+", line)[0])
        print(f"{len(shortest_directions)=}")
        print("int =", int(re.findall(r"\d+", line)[0]))
        print("-" * 100)

print(ans)

