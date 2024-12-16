def check_horizontal_forward(grid,i,j):
    word='XMAS'
    for col in range(j,j+4):
        if not( col<len(grid[0]) and grid[i][col]==word[col-j]):
            return False
    return True

def check_horizontal_backward(grid,i,j):
    word='XMAS'
    for col in range(j,j-4,-1):
        if not( col>=0 and grid[i][col]==word[j-col]):
            return False
    return True


def check_vertical_forward(grid,i,j):
    word='XMAS'
    for row in range(i,i+4):
        if not( row<len(grid) and grid[row][j]==word[row-i]):
            return False
    return True

def check_vertical_backward(grid,i,j):
    word='XMAS'
    for row in range(i,i-4,-1):
        if not( row>=0 and grid[row][j]==word[i-row]):
            return False
    return True

def check_diagonal_forward(grid,i,j):
    word='XMAS'
    for row,col in zip(range(i,i+4),range(j,j+4)):
        if not( row<len(grid) and col<len(grid[0]) and grid[row][col]==word[row-i]):
            return False
    return True

def check_diagonal_backward(grid,i,j):
    word='XMAS'
    for row,col in zip(range(i,i-4,-1),range(j,j-4,-1)):
        if not( row>=0 and col>=0 and grid[row][col]==word[i-row]):
            return False
    return True

def check_anti_diagonal_forward(grid,i,j):
    word='XMAS'
    for row,col in zip(range(i,i+4),range(j,j-4,-1)):
        if not( row<len(grid) and col>=0 and grid[row][col]==word[row-i]):
            return False
    return True

def check_anti_diagonal_backward(grid,i,j):
    word='XMAS'
    for row,col in zip(range(i,i-4,-1),range(j,j+4)):
        if not( row>=0 and col<len(grid[0]) and grid[row][col]==word[i-row]):
            return False
    return True

ans=0
with open("input.txt",'r') as f:
    grid = [x.strip() for x in f.readlines()]

    #Search for "XMAS" in the grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]=='X':
                #Worth checking from here

                if check_horizontal_forward(grid,i,j):
                    ans+=1
                if check_horizontal_backward(grid,i,j):
                    ans+=1
                
                if check_vertical_forward(grid,i,j):
                    ans+=1
                if check_vertical_backward(grid,i,j):
                    ans+=1

                if check_diagonal_forward(grid,i,j):    
                    ans+=1
                if check_diagonal_backward(grid,i,j):
                    ans+=1
                
                if check_anti_diagonal_forward(grid,i,j):
                    ans+=1
                if check_anti_diagonal_backward(grid,i,j):
                    ans+=1
print("ANSWER:",ans)
