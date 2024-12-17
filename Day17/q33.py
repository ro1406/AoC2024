"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q33.py (c) 2024
Desc: description
Created:  2024-12-17T04:41:14.385Z
Modified: 2024-12-17T07:42:05.553Z
"""

import pandas as pd

def get_operand_value(a, b, c, operand):
    if operand in [0, 1, 2, 3]:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    print("ERROR IN OPERAND")
    return -1


a, b, c = 0, 0, 0
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
print('program:',program)

outputs = []
dic={'pc':[],'opcode':[],'operand_literal':[],'operand_combo':[],'a':[],'b':[],'c':[]}
counter = 0
while counter < len(program):
    if len(outputs)<2:
        dic['pc'].append(counter)
        dic['opcode'].append(program[counter])
        dic['operand_literal'].append(program[counter+1])
        dic['operand_combo'].append(get_operand_value(a, b, c, program[counter + 1]))
        dic['a'].append(a)
        dic['b'].append(b)
        dic['c'].append(c)
    
    opcode = program[counter]
    combo_operand = get_operand_value(a, b, c, program[counter + 1])
    literal_operand = program[counter + 1]
    #2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0
    if opcode == 0:
        a = int(a // 2**combo_operand)
        counter += 2
    elif opcode == 1:
        b ^= literal_operand
        counter += 2
    elif opcode == 2:
        b = combo_operand % 8
        counter += 2
    elif opcode == 3:
        if a == 0:
            counter += 2
            continue
        else:
            counter = literal_operand
    elif opcode == 4:
        b = b ^ c
        counter += 2
    elif opcode == 5:
        val = combo_operand % 8
        outputs.append(str(val))
        counter += 2
    elif opcode == 6:
        b = int(a // 2**combo_operand)
        counter += 2
    elif opcode == 7:
        c = int(a // 2**combo_operand)
        counter += 2
    else:
        print("Invalid opcode")

print(",".join(outputs))

print(pd.DataFrame(dic))
