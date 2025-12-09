from collections import Counter,defaultdict


def get_score(grid):
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                score += 100 * i + j
    return score


move_coords = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


grid = []
moves = ""
reading_grid = True
with open("input.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            reading_grid = False
        if reading_grid:
            grid.append(list(line.replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]").strip()))
        else:
            moves += line.strip()

# for x in grid:
#     print("".join(x))
# print(len(moves))
# print(len(grid), len(grid[0]))
# print(get_score(grid))
# print(Counter(moves))
# 1_504_503 too low
# 1_520_401 too high

pos = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            grid[i][j] ='.'
            pos = (i, j)
            break

print("Start position:", pos)
for move in moves[:]:
    i,j = pos
    if move=='<':
        k=j-1
        while grid[i][k]==']':
            k-=2 
        if grid[i][k]=='.':
            for l in range(k,j):
                grid[i][l]=grid[i][l+1]
            pos = (i,j-1)

    elif move=='>':
        k=j+1
        while grid[i][k]=='[':
            k+=2 
        if grid[i][k]=='.':
            for l in reversed(range(j+1,k+1)):
                grid[i][l]=grid[i][l-1]
            pos = (i,j+1)

    elif move=='^':
        q={(i-1,j)}
        rows = defaultdict(set)
        while q:
            x,y=q.pop()
            if grid[x][y]=='#':
                break
            elif grid[x][y]==']':
                rows[x]|={y-1,y}
                q|={(x-1,y),(x-1,y-1)}
            elif grid[x][y]=='[':
                rows[x]|={y,y+1}
                q|={(x-1,y),(x-1,y+1)}
            elif grid[x][y]=='.':
                rows[x].add(y)
        else:
            for x in sorted(rows):
                for y in rows[x]:
                    grid[x][y]=grid[x+1][y] if y in rows[x+1] else '.'
            pos=(i-1,j)

    elif move=='v':
        q={(i+1,j)}
        rows = defaultdict(set)
        while q:
            x,y=q.pop()
            if grid[x][y]=='#':
                break
            elif grid[x][y]==']':
                rows[x]|={y-1,y}
                q|={(x+1,y),(x+1,y-1)}
            elif grid[x][y]=='[':
                rows[x]|={y,y+1}
                q|={(x+1,y),(x+1,y+1)}
            elif grid[x][y]=='.':
                rows[x].add(y)
        else:
            for x in reversed(sorted(rows)):
                for y in rows[x]:
                    grid[x][y]=grid[x-1][y] if y in rows[x-1] else '.'
            pos=(i+1,j)




# for x in grid:
#     print("".join(x))
# print(moves)
print(get_score(grid))
