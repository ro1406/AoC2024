from collections import Counter
with open("input1.txt",'r') as f:
    lines = f.readlines()
    x,y = zip(*[map(int,i.split()) for i in lines])
    x=list(sorted(list(x)))
    y=list(sorted(list(y)))
    
    counts = Counter(y)

    ans=0
    for loc in x:
        ans+= loc*counts[loc]

    print(ans)
