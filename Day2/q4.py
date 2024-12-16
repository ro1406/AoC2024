def is_valid(arr):
    inc,dec=False,False
    for i in range(len(arr)-1):
        diff = arr[i+1]-arr[i]
        if abs(diff)<1 or abs(diff)>3:
            return False
        if i==0:
            if diff>0:
                inc=True
            else:
                dec=True
        if diff>0 and not inc:
            return False
        if diff<0 and not dec:
            return False
    return True


ans=0
with open("input.txt",'r') as f:
    for line in f.readlines():
        arr=list(map(int,line.split()))
        if is_valid(arr): 
            ans+=1
            continue
        #Is the array valid if i remove the ith element
        for i in range(len(arr)):
            arr2=arr.copy()
            arr2.pop(i)
            if is_valid(arr2):
                ans+=1
                break

print(ans)