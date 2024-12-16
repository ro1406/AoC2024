
def find_guard(grid):
    guard = '<>^v'
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in guard:
                #Found the guard, need to find the direction
                if grid[i][j]=='<':
                    return i,j,'L'
                elif grid[i][j]=='^':
                    return i,j,'U'
                elif grid[i][j]=='v':
                    return i,j,'D'
                else:
                    return i,j,'R'
    return -1,-1,'X' #Error


dirs={'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
next_dir={'U':'R','D':'L','L':'U','R':'D'}


grid=[]
with open("input.txt",'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))
print(len(grid),len(grid[0]))

posx,posy,dir=find_guard(grid)
if dir=='X': print("ERROR DIRECTION WAS X")
visited=set()
visited.add((posx,posy))
while posx<len(grid) and posy<len(grid[0]):

    #Move gaurd till we find '#'
    while posx+dirs[dir][0]<len(grid) and posy+dirs[dir][1]<len(grid[0]) and \
            grid[posx+dirs[dir][0]][posy+dirs[dir][1]]!='#':
        posx+=dirs[dir][0]
        posy+=dirs[dir][1]
        visited.add((posx,posy))
 
    #If we're gonna go out of bounds then break
    if posx+dirs[dir][0]>=len(grid) or posy+dirs[dir][1]>=len(grid[0]):
        break

    #Move gaurd in next direction
    dir=next_dir[dir]

print(len(visited))
