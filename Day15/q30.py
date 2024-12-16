from collections import Counter
def get_score(grid):
    score=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='[':
                score+=100*i+j
    return score


move_coords = {'^':(-1,0),'v':(1,0),'<':(0,-1),'>':(0,1)}
    
# def try_and_move(pos,move,grid):
#     dx,dy = move_coords[move]
#     new_pos = (pos[0]+dx,pos[1]+dy)
#     # print(f"Called TAM on {pos=}, {move=}, {new_pos=}, {''.join(grid[pos[0]])=}")

#     if not(0<=pos[0]+dx<len(grid) and 0<=pos[1]+dy<len(grid[0])):
#         return pos,False,grid
    
#     x,y = new_pos
    
#     #Wall in front so cant move the object
#     if grid[x][y]=='#':
#         return pos,False,grid

#     #Block in front, so recursively call try and move on the block first
#     if grid[x][y] in '[]':
#         # print("Bracket next door, recursive calling...")
#         block_pos, moved, grid = try_and_move((x,y),move,grid)
#         # print("Grid moved. Now row is:",''.join(grid[pos[0]]),f'{pos=}, {move=}, {new_pos=}')
#         if not moved:
#             return pos,False,grid


#     #Empty space in front so move the object
#     if grid[x][y]=='.':
#         # print("Its a dot")
#         # check if its the @ moving or the []
#         if grid[pos[0]][pos[1]]=='@':
#             grid[x][y] = grid[pos[0]][pos[1]]
#             grid[pos[0]][pos[1]] = '.'
#             return (x,y),True,grid
#         else:
#             # print("Its not an @")
#             #Only move the [] if the other part of it can also move
#             bracket_map={']':-1,'[':1}
#             if move in '^v':
#                 # print("It is up down")
#                 # if grid[pos[0]][pos[1]] in bracket_map:
#                 partner_offset = bracket_map[grid[pos[0]][pos[1]]]
#                 #Move myself
#                 grid[x][y] = grid[pos[0]][pos[1]]
#                 grid[pos[0]][pos[1]] = '.'

#                 if grid[pos[0]][pos[1]+partner_offset] not in bracket_map:
#                     #My partner has already moved before I did
#                     return (x,y),True,grid
#                 #Try and move partner
#                 partner_pos, partner_moved, grid = try_and_move((pos[0],pos[1]+partner_offset),move,grid)
#                 if not partner_moved:
#                     #Undo my move
#                     grid[pos[0]][pos[1]] = grid[x][y]
#                     grid[x][y] = '.'
#                     return pos,False,grid
#                 else:
#                     #Partner has moved too so return True
#                     return (x,y),True,grid
#             else:
#                 # print("it is left right")
#                 #Moving sideways
#                 partner_offset = bracket_map[grid[pos[0]][pos[1]]]
#                 #Move myself
#                 grid[x][y] = grid[pos[0]][pos[1]]
#                 grid[pos[0]][pos[1]] = '.'
#                 return (x,y),True,grid
     
     
def try_and_move(pos,move,grid):
    dx,dy = move_coords[move]
    new_pos = (pos[0]+dx,pos[1]+dy)
    # print(f"Called TAM on {pos=}, {move=}, {new_pos=}, {''.join(grid[pos[0]])=}")

    if not(0<=pos[0]+dx<len(grid) and 0<=pos[1]+dy<len(grid[0])):
        return pos,False,grid
    
    x,y = new_pos
    
    #Wall in front so cant move the object
    if grid[x][y]=='#':
        return pos,False,grid

    #Block in front, so recursively call try and move on the block first
    if grid[x][y] in '[]':
        if move in '<>':
            # print("Bracket next door, recursive calling...")
            block_pos, moved, grid = try_and_move((x,y),move,grid)
            # print("Grid moved. Now row is:",''.join(grid[pos[0]]),f'{pos=}, {move=}, {new_pos=}')
            if not moved:
                return pos,False,grid
        else:
            # Ensure both parts of the box can move
            bracket_map = {'[': 1, ']': -1}
            partner_offset = bracket_map[grid[x][y]]
            partner_pos = (x, y + partner_offset)
            new_partner_pos = (partner_pos[0] + dx, partner_pos[1] + dy)

            # Check if the partner exists and can also move
            if not (0 <= new_partner_pos[0] < len(grid) and 0 <= new_partner_pos[1] < len(grid[0])):
                return pos, False, grid
            if grid[new_partner_pos[0]][new_partner_pos[1]] == '#':
                return pos, False, grid
            if grid[new_partner_pos[0]][new_partner_pos[1]] in '[]':
                block_pos, moved, grid = try_and_move(new_partner_pos, move, grid)
                if not moved:
                    return pos, False, grid

            # Move both parts of the box
            grid[x][y] = '.'
            grid[new_pos[0]][new_pos[1]] = grid[pos[0]][pos[1]]

            grid[partner_pos[0]][partner_pos[1]] = '.'
            grid[new_partner_pos[0]][new_partner_pos[1]] = grid[partner_pos[0]][partner_pos[1]]

            return new_pos, True, grid


    #Empty space in front so move the object
    if grid[x][y]=='.':
        # print("Its a dot")
        # check if its the @ moving or the []
        if grid[pos[0]][pos[1]]=='@':
            grid[x][y] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = '.'
            return (x,y),True,grid
        else:
            # print("Its not an @")
            #Only move the [] if the other part of it can also move
            bracket_map={']':-1,'[':1}
            if move in '^v':
                # print("It is up down")
                # if grid[pos[0]][pos[1]] in bracket_map:
                partner_offset = bracket_map[grid[pos[0]][pos[1]]]
                #Move myself
                grid[x][y] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = '.'

                if grid[pos[0]][pos[1]+partner_offset] not in bracket_map:
                    #My partner has already moved before I did
                    return (x,y),True,grid
                #Try and move partner
                partner_pos, partner_moved, grid = try_and_move((pos[0],pos[1]+partner_offset),move,grid)
                if not partner_moved:
                    #Undo my move
                    grid[pos[0]][pos[1]] = grid[x][y]
                    grid[x][y] = '.'
                    return pos,False,grid
                else:
                    #Partner has moved too so return True
                    return (x,y),True,grid
            else:
                # print("it is left right")
                #Moving sideways
                partner_offset = bracket_map[grid[pos[0]][pos[1]]]
                #Move myself
                grid[x][y] = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = '.'
                return (x,y),True,grid



    
    
    
    

grid=[]
moves=''
reading_grid=True
with open('input.txt','r') as f:
    for line in f.readlines():
        if line=='\n':
            reading_grid=False
        if reading_grid:
            grid.append(list(line.replace("#","##").replace('.','..').replace('@','@.').replace('O','[]').strip()))
        else:
            moves+=line.strip()

for x in grid:
    print(''.join(x))
print(len(moves))
print(len(grid),len(grid[0]))
print(get_score(grid))
print(Counter(moves))
#1_504_503 too low

pos = (0,0)
for i in range(len(grid)): 
    for j in range(len(grid[i])): 
        if grid[i][j]=='@': 
            pos=(i,j)
            break

print("Start position:",pos)
x,y=pos
for move in moves:
    
    new_pos, moved, grid = try_and_move(pos,move,grid)
    # if moved==False:
    #     print("Didnt move!")
    #     print(pos)
    print(move)
    for x in grid:
        print(''.join(x))
    pos=new_pos

for x in grid:
    print(''.join(x))
print(moves)
print(get_score(grid))
