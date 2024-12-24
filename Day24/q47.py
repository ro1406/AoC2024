"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q47.py (c) 2024
Desc: description
Created:  2024-12-24T04:52:40.762Z
Modified: 2024-12-24T05:33:43.256Z
"""
from time import time
from tqdm import tqdm
from collections import deque
import re


def solve(v1,v2,op):
    if op=='AND':
        return v1&v2
    elif op=='OR':
        return v1|v2
    elif op=='XOR':
        return v1^v2
    else:
        raise Exception("INVALID OP")

def eval_op(v1,op, v2,res,dic,rules):
    if v1 in dic and v2 in dic:
        dic[res] = solve(dic[v1],dic[v2],op)
        # return dic[res]
        return dic[res]

    if v1 not in dic:
        #Recursively call this on the operation with v1 as sol
        op_with_V1_sol = [x for x in rules if x[-1]==v1][0]
        eval_op(op_with_V1_sol[0],op_with_V1_sol[1],op_with_V1_sol[2],v1,dic,rules)

    if v2 not in dic:
        #Recursively call this on the operation with v2 as sol
        op_with_V2_sol = [x for x in rules if x[-1]==v2][0]
        eval_op(op_with_V2_sol[0],op_with_V2_sol[1],op_with_V2_sol[2],v2,dic,rules)

    dic[res] = solve(dic[v1],dic[v2],op)
    return dic[res]


read_inputs=True
rules=[]
dic={}
with open("input.txt", "r") as f:
    for line in f.readlines():
        if line=='\n':
            read_inputs=False
            print(dic)
            continue
        if read_inputs:
            key,val = line.strip().split(": ")
            dic[key]=int(val)
        else:
            pattern = r'((?:[a-zA-Z0-9]{1,3})(?:\d{0,2})) (AND|XOR|OR) ((?:[a-zA-Z0-9]{1,3})(?:\d{0,2})) -> ((?:[a-zA-Z0-9]{1,3})(?:\d{0,2}))'
            matches = re.findall(pattern, line)
            v1,op,v2,res = matches[0]
            rules.append((v1,op,v2,res))


ans=''
for i in [f'0{i}' for i in range(0,10)] + list(map(str,range(10,99))):
    #Find the rule which ends with z+{i}
    
    rule_with_zi_result = [x for x in rules if x[-1]=='z'+i]
    if not rule_with_zi_result:
        break
    rule_with_zi_result=rule_with_zi_result[0]
    res = eval_op(rule_with_zi_result[0],rule_with_zi_result[1],rule_with_zi_result[2],rule_with_zi_result[3],dic,rules)
    ans = str(res) + ans
        



print(ans)
print(int(ans,2))

        