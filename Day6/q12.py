from tqdm import tqdm
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


def move_guard(grid):
    dirs={'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
    next_dir={'U':'R','D':'L','L':'U','R':'D'}
    posx,posy,dir=find_guard(grid)
    if dir=='X': print("ERROR DIRECTION WAS X")
    visited=set()
    visited.add((posx,posy,dir))
    loop=False
    while posx<len(grid) and posy<len(grid[0]):

        #Move gaurd till we find '#'
        while 0<=posx+dirs[dir][0]<len(grid) and 0<=posy+dirs[dir][1]<len(grid[0]) and \
                grid[posx+dirs[dir][0]][posy+dirs[dir][1]]!='#':
            posx+=dirs[dir][0]
            posy+=dirs[dir][1]
    
        #If we're gonna go out of bounds then break
        if posx+dirs[dir][0]>=len(grid) or posy+dirs[dir][1]>=len(grid[0]) or 0>posx+dirs[dir][0] or 0>posy+dirs[dir][1]:
            break

        if (posx,posy,dir) in visited:
            loop=True
            break

        #Only add the visited node when we make a direction change, not every step
        visited.add((posx,posy,dir))
        #Move gaurd in next direction
        dir=next_dir[dir]

    #Return if the guard was stuck in a loop
    return loop



grid=[]
with open("input.txt",'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))
print(len(grid),len(grid[0]))

ans=0
for i in tqdm(range(len(grid))):
    for j in range(len(grid[i])):
        if grid[i][j]=='.':
            #Try to place a box here and then move_gaurd and see if he hits a loop
            grid[i][j]='#'
            looped = move_guard(grid)
            grid[i][j]='.'
            if looped:
                ans+=1

print(ans)
#The algorithm returns True when the box is placed right in front of the guard. This is wrong, so -1 to omit that case
print('Without considering the spot right infront of the guard:',ans-1)
