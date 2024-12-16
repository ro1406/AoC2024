def check_diagonal_forward(grid,i,j):
    word='MAS'
    if i>=len(grid) or j>=len(grid[0]):
        return False
    for row,col in zip(range(i,i+len(word)),range(j,j+len(word))):
        if not( row<len(grid) and col<len(grid[0]) and grid[row][col]==word[row-i]):
            return False
    return True

def check_diagonal_backward(grid,i,j):
    word='MAS'
    if i>=len(grid) or j>=len(grid[0]):
        return False
    for row,col in zip(range(i,i-len(word),-1),range(j,j-len(word),-1)):
        if not( row>=0 and col>=0 and grid[row][col]==word[i-row]):
            return False
    return True

def check_anti_diagonal_forward(grid,i,j):
    word='MAS'
    if i>=len(grid) or j>=len(grid[0]):
        return False
    for row,col in zip(range(i,i+len(word)),range(j,j-len(word),-1)):
        if not( row<len(grid) and col>=0 and grid[row][col]==word[row-i]):
            return False
    return True

def check_anti_diagonal_backward(grid,i,j):
    word='MAS'
    if i>=len(grid) or j>=len(grid[0]):
        return False
    for row,col in zip(range(i,i-len(word),-1),range(j,j+len(word))):
        if not( row>=0 and col<len(grid[0]) and grid[row][col]==word[i-row]):
            return False
    return True

ans=0
with open("input.txt",'r') as f:
    grid = [x.strip() for x in f.readlines()]

    #Search for "XMAS" in the grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            #Worth checking from here

            #DF -> LT RD
            #DB -> RD LT
            #AD -> RT LD
            #ADB -> LD RT

            # MAS x MAS
            if check_diagonal_forward(grid,i,j) and check_anti_diagonal_forward(grid,i,j+2):
                ans+=1
            #MAS x SAM
            if check_diagonal_forward(grid,i,j) and check_anti_diagonal_backward(grid,i+2,j):
                ans+=1
            #SAM x MAS
            if check_diagonal_backward(grid,i+2,j+2) and check_anti_diagonal_forward(grid,i,j+2):
                ans+=1
            #SAM x SAM
            if check_diagonal_backward(grid,i+2,j+2) and check_anti_diagonal_backward(grid,i+2,j):
                ans+=1

print("ANSWER:",ans)
