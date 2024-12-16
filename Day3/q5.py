import re
ans=0
with open("input.txt",'r') as f:
    for line in f.readlines():
        #Match mul(x,y)
        pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'

        nums = re.findall(pattern,line)
        for x,y in nums:
            ans+= int(x)*int(y)
print(ans)