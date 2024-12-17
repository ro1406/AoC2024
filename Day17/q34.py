"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q33.py (c) 2024
Desc: description
Created:  2024-12-17T04:41:14.385Z
Modified: 2024-12-17T08:18:56.232Z
"""


def get_val(a):
    # This function is based on my input program
    # I did a trace table to identify the mathematical formula for the program (one iteration)
    # Avoids using loops to check each value
    d = (a % 8) ^ 5
    val = (d ^ int(a / (2**d)) ^ 6) % 8
    return val


with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            a = int(line.split()[-1].strip())
        elif i == 1:
            b = int(line.split()[-1].strip())
        elif i == 2:
            c = int(line.split()[-1].strip())
        elif "Program" in line:
            program = list(map(int, line.split()[-1].strip().split(",")))

print(f"{a=},{b=},{c=}")
print("program:", program)


ans = [0]
for p in reversed(program):
    temp_ans = []
    for x in ans:
        for a in range(8):
            # Try exploring this answer with all possible values of a
            # Each number "a" is only 3 bits so we just need to add those 3 to the end and see if we get the right output
            val_to_check = (x << 3) + a
            val = get_val(val_to_check)
            if val == p:
                # There may be more than one answer that gives the right digit output, so we need to consider all possibilities
                # Could have recursively considered but who has the time for that?
                temp_ans.append(val_to_check)
    ans = temp_ans
print(ans)
print(min(ans))
