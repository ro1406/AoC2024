"""
Author: Rohan Mitra (rohan.mitra@dubizzle.com)
q43.py (c) 2024
Desc: description
Created:  2024-12-22T09:39:51.741Z
Modified: 2024-12-22T09:48:46.734Z
"""
from time import time

def get_next_secret_num(num):
    first = ((64*num)^num)%16777216
    second = ((int(first/32))^first)%16777216
    third = ((2048*second)^second)%16777216

    return third

t0=time()
ans=0
with open("input.txt",'r') as f:
    for line in f.readlines():
        num=int(line.strip())
        orig_num = num
        for _ in range(2000):
            secret_num = get_next_secret_num(num)
            num = secret_num
        
        # print(f"{orig_num}: {secret_num}")
        ans+=secret_num

print(ans)
print("Time taken:",time()-t0)
        