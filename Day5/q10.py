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
            update_made=False
            for i,x in enumerate(update):
                index_to_insert=float('inf')
                if x in rules:
                    #There is a rule about this number
                    #Check if any numbers in the rule are present BEFORE the current number in update
                    for y in sorted(rules[x]):
                        try:
                            y_idx = update.index(y)
                        except:
                            #Not present in update, ignore
                            continue
                        if y_idx<i:
                            #Invalid update -> will need to move x to a lower index
                            index_to_insert=min(index_to_insert,y_idx)
                            
                    if index_to_insert<100_000:
                        #Remove x from update and insert it at index_to_insert
                        update.remove(x)
                        update.insert(index_to_insert,x)
                        update_made=True

            if update_made:
                #Save middle number
                ans+=update[len(update)//2]
print(ans)
