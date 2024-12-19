"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q35.py (c) 2024
Desc: description
Created:  2024-12-19T05:04:15.466Z
Modified: 2024-12-19T05:34:06.274Z
"""


def can_find(substrs, query):
    substrs_set = set(substrs)
    dp = [0] * (len(query) + 1)  # The number of ways to form the prefix until index [i]
    dp[0] = 1  # Empty string can always be formed

    for i in range(1, len(query) + 1):
        for substr in substrs_set:
            # for each substring, if the last part of the query is equal to the substring then i can make this part of the query
            if i >= len(substr) and query[i - len(substr) : i] == substr:
                dp[i] += dp[i - len(substr)]

    return dp[len(query)]


def can_find_recursive(substrs, query, memo={}):
    substrs_set = set(substrs)
    if query in memo:
        return memo[query]
    if not query:
        return 1

    ans = 0
    for substr in substrs_set:
        if query.startswith(substr):
            ans += can_find_recursive(substrs, query[len(substr) :], memo)

    memo[query] = ans
    return ans


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
            ans += can_find_recursive(substrs, query)

print(ans)
