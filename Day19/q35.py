"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q35.py (c) 2024
Desc: description
Created:  2024-12-19T05:04:15.466Z
Modified: 2024-12-19T05:31:55.898Z
"""


def can_find(substrs, query):
    substrs_set = set(substrs)
    dp = [False] * (len(query) + 1)  # The prefix until index [i] can be formed
    dp[0] = True  # Empty string can always be formed

    for i in range(1, len(query) + 1):
        for substr in substrs_set:
            # prefix until i-len(substr) can be formed and the remaining part is equal to substr
            if i >= len(substr) and dp[i - len(substr)] and query[i - len(substr) : i] == substr:
                dp[i] = True
                break  # No need to check further if dp[i] is True

    return dp[len(query)]

def can_find_recursive(substrs, query,memo={}):
    substrs_set = set(substrs)
    if query in memo:
        return memo[query]
    if not query: return True

    for substr in substrs_set:
        if query.startswith(substr):
            if can_find_recursive(substrs, query[len(substr):],memo):
                memo[query]=True
                return True

    memo[query]=False
    return False
    


ans = 0
with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            substrs = tuple(line.strip().split(", "))
            print(substrs)
        elif i == 1:
            continue
        else:
            query = line.strip()
            # print(query,end=' ')
            # canfindres = can_find(substrs, query)
            canfindres = can_find_recursive(substrs, query)
            # print(canfindres)
            if canfindres:
                ans += 1

print(ans)
