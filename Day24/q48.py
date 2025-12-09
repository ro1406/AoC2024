from time import time
from tqdm import tqdm
from collections import deque
import re


def solve(v1, v2, op):
    if op == "AND":
        return v1 & v2
    elif op == "OR":
        return v1 | v2
    elif op == "XOR":
        return v1 ^ v2
    else:
        raise Exception("INVALID OP")


def eval_op(v1, op, v2, res, dic, rules):
    if v1 in dic and v2 in dic:
        dic[res] = solve(dic[v1], dic[v2], op)
        return dic[res]

    if v1 not in dic:
        # Recursively call this on the operation with v1 as sol
        op_with_V1_sol = [x for x in rules if x[-1] == v1][0]
        eval_op(op_with_V1_sol[0], op_with_V1_sol[1], op_with_V1_sol[2], v1, dic, rules)

    if v2 not in dic:
        # Recursively call this on the operation with v2 as sol
        op_with_V2_sol = [x for x in rules if x[-1] == v2][0]
        eval_op(op_with_V2_sol[0], op_with_V2_sol[1], op_with_V2_sol[2], v2, dic, rules)

    dic[res] = solve(dic[v1], dic[v2], op)
    return dic[res]


read_inputs = True
rules = []
dic = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            read_inputs = False
            print(dic)
            continue
        if read_inputs:
            key, val = line.strip().split(": ")
            dic[key] = int(val)
        else:
            pattern = r"((?:[a-zA-Z0-9]{1,3})(?:\d{0,2})) (AND|XOR|OR) ((?:[a-zA-Z0-9]{1,3})(?:\d{0,2})) -> ((?:[a-zA-Z0-9]{1,3})(?:\d{0,2}))"
            matches = re.findall(pattern, line)
            v1, op, v2, res = matches[0]
            rules.append((v1, op, v2, res))


ans = ""
for i in [f"0{i}" for i in range(0, 10)] + list(map(str, range(10, 99))):
    # Find the rule which ends with z+{i}

    rule_with_zi_result = [x for x in rules if x[-1] == "z" + i]
    if not rule_with_zi_result:
        break
    rule_with_zi_result = rule_with_zi_result[0]
    res = eval_op(
        rule_with_zi_result[0], rule_with_zi_result[1], rule_with_zi_result[2], rule_with_zi_result[3], dic, rules
    )
    ans = str(res) + ans

print(ans)
print(int(ans, 2))


##### verify if this makes sense x+y=z

x_bin = ""
y_bin = ""
z_bin = ""

for i in [f"0{i}" for i in range(0, 10)] + list(map(str, range(10, 45))):

    x_bin = str(dic["x" + i]) + x_bin
    y_bin = str(dic["y" + i]) + y_bin
    z_bin = str(dic["z" + i]) + z_bin

# print(x_bin,y_bin,z_bin)
x, y, z = int(x_bin, 2), int(y_bin, 2), int(z_bin, 2)

x_plus_y_binary = f"{x+y:b}"
print("RORO")
print(x_plus_y_binary)


def nidal(v1, op, v2, ans, target, issues=list(), depth=0):
    # print(f"nidal called with: {v1=},{op=},{v2=},{ans=} -> {dic[v1]} {op} {dic[v2]} = {dic[ans]} | {target=},{issues=},{depth=}")
    # No issue if answer==real
    if dic[ans] == target or not [x for x in rules if x[-1] == v1] or not [x for x in rules if x[-1] == v2]:
        return issues

    # Issue is if the answer is not equal to target value
    if op == "AND":
        if target == 1:  # Wanted it to be a 1 but it was a 0
            # Recurse on zero elements
            pt1 = []
            pt2 = []
            if dic[v1] == 0:
                # Get v1
                rule_with_v1_result = [x for x in rules if x[-1] == v1][0]
                pt1 = nidal(
                    rule_with_v1_result[0],
                    rule_with_v1_result[1],
                    rule_with_v1_result[2],
                    rule_with_v1_result[3],
                    1,
                    issues + [(v1, depth)],
                    depth + 1,
                )
            if dic[v2] == 0:
                # Get v2
                rule_with_v2_result = [x for x in rules if x[-1] == v2][0]
                pt2 = nidal(
                    rule_with_v2_result[0],
                    rule_with_v2_result[1],
                    rule_with_v2_result[2],
                    rule_with_v2_result[3],
                    1,
                    issues + [(v2, depth)],
                    depth + 1,
                )
            return pt1 + pt2

        else:  # Wanted it to be a 0 but it was a 1 -> x=1,y=1 -> z=1
            # Recurse on both elements
            rule_with_v1_result = [x for x in rules if x[-1] == v1][0]
            rule_with_v2_result = [x for x in rules if x[-1] == v2][0]
            return nidal(
                rule_with_v1_result[0],
                rule_with_v1_result[1],
                rule_with_v1_result[2],
                rule_with_v1_result[3],
                0,
                issues + [(v1, depth)],
                depth + 1,
            ) + nidal(
                rule_with_v2_result[0],
                rule_with_v2_result[1],
                rule_with_v2_result[2],
                rule_with_v2_result[3],
                0,
                issues + [(v2, depth)],
                depth + 1,
            )

    elif op == "OR":
        if target == 0:  # Wanted it to be a 0 but it was a 1 -> 01,10,11
            # Recurse on non zero elements
            pt1 = []
            pt2 = []
            if dic[v1] != 0:
                # Get v1
                rule_with_v1_result = [x for x in rules if x[-1] == v1][0]
                pt1 = nidal(
                    rule_with_v1_result[0],
                    rule_with_v1_result[1],
                    rule_with_v1_result[2],
                    rule_with_v1_result[3],
                    0,
                    issues + [(v1, depth)],
                    depth + 1,
                )
            if dic[v2] != 0:
                # Get v2
                rule_with_v2_result = [x for x in rules if x[-1] == v2][0]
                pt2 = nidal(
                    rule_with_v2_result[0],
                    rule_with_v2_result[1],
                    rule_with_v2_result[2],
                    rule_with_v2_result[3],
                    0,
                    issues + [(v2, depth)],
                    depth + 1,
                )
            return pt1 + pt2

        else:  # Wanted it to be a 1 but it was a 0 -> x=0,y=0 -> z=0
            # Recurse on both elements
            rule_with_v1_result = [x for x in rules if x[-1] == v1][0]
            rule_with_v2_result = [x for x in rules if x[-1] == v2][0]
            return nidal(
                rule_with_v1_result[0],
                rule_with_v1_result[1],
                rule_with_v1_result[2],
                rule_with_v1_result[3],
                1,
                issues + [(v1, depth)],
                depth + 1,
            ) + nidal(
                rule_with_v2_result[0],
                rule_with_v2_result[1],
                rule_with_v2_result[2],
                rule_with_v2_result[3],
                1,
                issues + [(v2, depth)],
                depth + 1,
            )

    else:
        # XOR
        # wanted it to be a 1 but it was a 0 -> 00 or 11 -> recurse on both
        # Wanted it to be a 0 but it was a 1 -> 01 or 10 -> recurse on both

        # Recurse on both
        rule_with_v1_result = [x for x in rules if x[-1] == v1][0]
        rule_with_v2_result = [x for x in rules if x[-1] == v2][0]
        return nidal(
            rule_with_v1_result[0],
            rule_with_v1_result[1],
            rule_with_v1_result[2],
            rule_with_v1_result[3],
            target,
            issues + [(v1, depth)],
            depth + 1,
        ) + nidal(
            rule_with_v2_result[0],
            rule_with_v2_result[1],
            rule_with_v2_result[2],
            rule_with_v2_result[3],
            target,
            issues + [(v2, depth)],
            depth + 1,
        )


issues_set = set()
for i, (z_real, z_pred) in enumerate(zip(x_plus_y_binary[::-1], ans[::-1])):
    if z_real != z_pred:
        print(f"{z_real=}, {z_pred=}")
        if 0 <= i <= 9:
            i = f"0{i}"
        rule_with_zi_result = [x for x in rules if x[-1] == "z" + str(i)]
        rule_with_zi_result = rule_with_zi_result[0]
        print(rule_with_zi_result)
        issues = nidal(
            rule_with_zi_result[0],
            rule_with_zi_result[1],
            rule_with_zi_result[2],
            rule_with_zi_result[3],
            int(z_real),
            list(),
            depth=0,
        )
        print(list(sorted(issues, key=lambda x: x[1], reverse=True)))
        print("-" * 100)
        for issue in issues:
            issues_set.add(issue)


issues_set = list(sorted(issues_set, key=lambda x: x[1], reverse=True))

print(issues_set)
print(len(issues_set))
print(",".join(x[0] for x in issues_set[:8]))
