with open("input1.txt",'r') as f:
    lines = f.readlines()
    x,y = zip(*[map(int,i.split()) for i in lines])
    x=list(sorted(list(x)))
    y=list(sorted(list(y)))
    
    print(sum(abs(x[i] - y[i]) for i in range(len(x))))