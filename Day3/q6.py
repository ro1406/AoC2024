import re
ans=0
with open("input.txt",'r') as f:
    do=True #Variable doesnt re-initialize for every line in the file
    #Match mul(x,y) or don't() or do()
    pattern = r"(?:mul\(([0-9]{1,3}),([0-9]{1,3})\))|(?:(don't)\(\))|(?:(do)\(\))"

    for line in f.readlines():
        commands = re.findall(pattern,line)    
        #Commands contains ('','','','')
        # index 2 is don't and 3 is do
        # index 0 and 1 are numbers if applicable
        for command in commands:
            if command[2] == "don't":
                do=False
            elif command[3] == "do":
                do=True
            else:
                if do:
                    ans+= int(command[0])*int(command[1])
print(ans)