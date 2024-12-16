
def get_score(grid):
    score=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='O':
                score+=100*i+j
    return score


move_coords = {'^':(-1,0),'v':(1,0),'<':(0,-1),'>':(0,1)}
    
def try_and_move(pos,move,grid):
    dx,dy = move_coords[move]
    new_pos = (pos[0]+dx,pos[1]+dy)

    if not(0<=pos[0]+dx<len(grid) and 0<=pos[1]+dy<len(grid[0])):
        return pos,False,grid
    
    x,y = new_pos

    #Block in front, so recursively call try and move on the block first
    if grid[x][y]=='O':
        block_pos, moved, grid = try_and_move((x,y),move,grid)
        if not moved:
            return pos,False,grid
        
    #Empty space in front so move the object
    if grid[x][y]=='.':
        grid[x][y] = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = '.'
        return (x,y),True,grid
    
    #Wall in front so cant move the object
    if grid[x][y]=='#':
        return pos,False,grid
    
    

grid=[]
moves=''
reading_grid=True
with open('input.txt','r') as f:
    for line in f.readlines():
        if line=='\n':
            reading_grid=False
        if reading_grid:
            grid.append(list(line.strip()))
        else:
            moves+=line.strip()

# for x in grid:
#     print(''.join(x))
# print(moves)

pos = (0,0)
for i in range(len(grid)): 
    for j in range(len(grid[i])): 
        if grid[i][j]=='@': 
            pos=(i,j)
            break

x,y=pos
for move in moves:
    
    new_pos, moved, grid = try_and_move(pos,move,grid)
    # if moved==False:
    #     print("Didnt move!")
    #     print(pos)
    # print(move)
    # for x in grid:
    #     print(''.join(x))
    pos=new_pos

for x in grid:
    print(''.join(x))
print(moves)
print(get_score(grid))
