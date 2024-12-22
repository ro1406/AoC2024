"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q43.py (c) 2024
Desc: description
Created:  2024-12-22T09:39:51.741Z
Modified: 2024-12-22T11:17:22.261Z
"""

from time import time
import pandas as pd
from tqdm import tqdm


def get_next_secret_num(num):
    first = ((64 * num) ^ num) % 16777216
    second = ((int(first / 32)) ^ first) % 16777216
    third = ((2048 * second) ^ second) % 16777216

    return third


t0 = time()

with open("input.txt", "r") as f:
    dic = {}
    for line in f.readlines():
        num = int(line.strip())
        orig_num = num
        dic[orig_num] = []

        for _ in range(2000):
            secret_num = get_next_secret_num(num)
            num = secret_num
            dic[orig_num].append(secret_num % 10)

df = pd.DataFrame(dic)
for col in df.columns:
    df[str(col) + "_diff"] = df[col].diff()

print(df.shape)
print(df.iloc[:20])

all_seqs = []

for col in [x for x in df.columns if "_" in str(x)]:
    temp_dict = {}
    for i in range(len(df[col]) - 4):
        seq = tuple(df[col].iloc[i : i + 4].to_list())
        if seq not in temp_dict:
            temp_dict[seq] = df[int(col.split("_")[0])].iloc[i + 3]

    all_seqs.append(temp_dict)

print(f"{len(all_seqs)=}")

ans = 0
unique_sequences = {key for d in all_seqs for key in d}
for seq in tqdm(unique_sequences):
    total = 0
    for dic in all_seqs:
        if seq in dic:
            total += dic[seq]
    ans = max(ans, total)

print(ans)
print("Time taken:", time() - t0)
