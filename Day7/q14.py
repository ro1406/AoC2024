from time import time

def recur(res,nums,curr_res):
    if curr_res>res:
        return False
    if len(nums)==0:
        return curr_res==res    
    return recur(res,nums[1:],curr_res+nums[0]) or recur(res,nums[1:],curr_res*nums[0]) or recur(res,nums[1:],int(str(curr_res)+str(nums[0])))


ans=0
t0=time()
with open("input.txt",'r') as f:
    for line in f.readlines():
        res,nums = line.strip().split(': ')
        nums = list(map(int,nums.split()))
        res = int(res)
        if recur(res,nums,0):
            ans+=res
print(ans)
print(time()-t0)