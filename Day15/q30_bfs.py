from collections import Counter


def get_score(grid):
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                score += 100 * i + j
    return score


move_coords = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

def try_and_move(pos, move, grid, boxes_to_move=[]):
    # Tell me if i can move this box in this direction or not - Dont actually move the box!
    # If i can move the box, then tell me which all boxes should be moved to which positions: [can_move,(box1_initial,box1_final),(box2_initial,box2_final)]
    dx, dy = move_coords[move]
    new_pos = (pos[0] + dx, pos[1] + dy)
    # print(f"Called TAM on {pos=}, {move=}, {new_pos=}, {''.join(grid[pos[0]])=}")

    if not (0 <= pos[0] + dx < len(grid) and 0 <= pos[1] + dy < len(grid[0])):
        return boxes_to_move + [False, pos, pos]

    x, y = new_pos
    bracket_map = {"]": -1, "[": 1}

    # Wall in front so cant move the object
    if grid[x][y] == "#":
        return boxes_to_move + [False, pos, pos]
    
    # OR check if wall infront of your partner
    if grid[pos[0]][pos[1]] in bracket_map:
        partner_offset = bracket_map[grid[pos[0]][pos[1]]]
        if move in "^v" and grid[x][y + partner_offset] == "#":
            # print("Partner has wall infront")
            # No wall infront of me but wall infront of my partner
            return boxes_to_move + [False, pos, pos]

    # Block in front, so recursively call try and move on the block first
    if grid[x][y] in "[]":
        # print("Bracket next door, recursive calling...")
        boxes_to_move_temp = try_and_move((x, y), move, grid)
        # print("Grid moved. Now row is:",''.join(grid[pos[0]]),f'{pos=}, {move=}, {new_pos=}')
        if not boxes_to_move_temp[-1][0]:
            return boxes_to_move + [False, pos, pos]

    # Empty space in front so move the object
    if grid[x][y] == ".":
        # print("Its a dot")
        # check if its the @ moving or the []
        if grid[pos[0]][pos[1]] == "@":
            # grid[x][y] = grid[pos[0]][pos[1]]
            # grid[pos[0]][pos[1]] = '.'
            return boxes_to_move + [True, pos, (x, y)]
        else:
            # print("Its not an @")
            # Only move the [] if the other part of it can also move

            if move in "^v":
                # print("It is up down")
                # if grid[pos[0]][pos[1]] in bracket_map:
                partner_offset = bracket_map[grid[pos[0]][pos[1]]]
                # Move myself
                # grid[x][y] = grid[pos[0]][pos[1]]
                # grid[pos[0]][pos[1]] = '.'

                if grid[pos[0]][pos[1] + partner_offset] not in bracket_map:
                    # My partner has already moved before I did
                    return boxes_to_move + [True, pos, (x, y)]
                # Try and move partner
                boxes_to_move_temp = try_and_move((pos[0], pos[1] + partner_offset), move, grid)
                if not boxes_to_move_temp[-1][0]:
                    # #Undo my move
                    # grid[pos[0]][pos[1]] = grid[x][y]
                    # grid[x][y] = '.'
                    return boxes_to_move + [False, pos, pos]
                else:
                    # Partner has moved too so return True
                    return boxes_to_move + [True, pos, (x, y)]
            else:
                # print("it is left right")
                # Moving sideways
                partner_offset = bracket_map[grid[pos[0]][pos[1]]]
                # Move myself
                # grid[x][y] = grid[pos[0]][pos[1]]
                # grid[pos[0]][pos[1]] = "."
                return boxes_to_move + [True, pos, (x, y)]


def move_boxes(boxes_to_move,grid):
    robot_x,robot_y=-1,-1
    grid_copy = grid.copy()
    for moved,oldij,newij in reversed(boxes_to_move):
        if grid[oldij[0]][oldij[1]]=='@':
            robot_x,robot_y = newij

        grid_copy[newij[0]][newij[1]] = grid[oldij[0]][oldij[1]]
        grid_copy[oldij[0]][oldij[1]] = '.'
        
    return grid_copy, (robot_x,robot_y)




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

for x in grid:
    print("".join(x))
print(len(moves))
print(len(grid), len(grid[0]))
print(get_score(grid))
print(Counter(moves))
# 1_504_503 too low
# 1_520_401 too high

pos = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            pos = (i, j)
            break

print("Start position:", pos)
x, y = pos
for move in moves:

    boxes_to_move = try_and_move(pos, move, grid)

    #If all can be moved then move
    if all(x[0] for x in boxes_to_move):
        grid,new_pos = move_boxes(boxes_to_move,grid)
    
    print(move)
    for x in grid:
        print("".join(x))
    pos = new_pos

for x in grid:
    print("".join(x))
print(moves)
print(get_score(grid))
