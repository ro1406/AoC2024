ans=0
rules={}
with open("input.txt",'r') as f:
    #Read until empty line
    reading_rules = True
    for line in f.readlines():
        if line == "\n":
            reading_rules=False
            continue
    
        if reading_rules:
            x,y = map(int,line.strip().split('|'))
            if x in rules:
                rules[x].append(y)
            else:
                rules[x]=[y]
        else:
            #Now we reading updates
            update = list(map(int,line.strip().split(',')))
            invalid=False
            for i,x in enumerate(update):
                if x in rules:
                    #There is a rule about this number
                    #Check if all numbers in the rule are present AFTER the current number in update
                    for y in sorted(rules[x]):
                        if y in update[:i]:
                            invalid=True

            if not invalid:
                #Save middle number
                ans+=update[len(update)//2]
print(ans)
