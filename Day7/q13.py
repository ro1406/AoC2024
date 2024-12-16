
def recur(res,nums,curr_res):
    if len(nums)==0:
        return curr_res==res    
    return recur(res,nums[1:],curr_res+nums[0]) or recur(res,nums[1:],curr_res*nums[0])


ans=0
with open("input.txt",'r') as f:
    for line in f.readlines():
        res,nums = line.strip().split(': ')
        nums = list(map(int,nums.split()))
        res = int(res)
        if recur(res,nums,0):
            ans+=res
print(ans)