ans=0
with open("input.txt",'r') as f:
    for line in f.readlines():
        arr=list(map(int,line.split()))
        inc,dec=False,False
        valid=True
        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if abs(diff)<1 or abs(diff)>3:
                valid=False
                break
            if i==0:
                if diff>0:
                    inc=True
                else:
                    dec=True
            if diff>0 and not inc:
                valid=False
                break
            if diff<0 and not dec:
                valid=False
                break
        
        if valid: ans+=1

print(ans)
            