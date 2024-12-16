from collections import deque

def dfs_iterative(i,j,grid):
    # Directions and their mappings
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    turn_cost = 1000
    forward_cost = 1

    # Initialize queue with starting position, direction, and score
    q = deque([(i, j, 'R', 0, [(i,j)])])  # Start at S facing East (Right)
    visited = {}
    best_paths=[]

    min_score = float('inf')  # Track the minimum score to the goal

    while q:
        x, y, curr_dir, curr_score, curr_path = q.popleft()

        # Check if we have reached the goal
        if grid[x][y] == 'E':
            if curr_score<=min_score:
                min_score=curr_score
                best_paths.append((curr_path,min_score))
            continue

        # Skip if we have visited this state with a better score
        if (x, y, curr_dir) in visited and visited[(x, y, curr_dir)] < curr_score:
            continue

        # Mark the current state as visited
        visited[(x, y, curr_dir)] = curr_score

        # Explore all possible directions
        for new_dir, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy

            # Check boundaries and obstacles
            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#'):
                continue

            # Calculate the new score
            new_score = curr_score + forward_cost
            if new_dir != curr_dir:  # Add turn cost if changing direction
                new_score += turn_cost

            # Add the new state to the queue
            q.append((nx, ny, new_dir, new_score, curr_path + [(nx,ny)]))

    return min_score if min_score != float('inf') else -1, [x[0] for x in best_paths if x[1]==min_score]  # Return -1 if no path found



grid=[]
with open("input.txt") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))
# print(grid)
best_score, best_paths = dfs_iterative(len(grid)-2,1,grid)
print(f"{best_score=}")
print(f"Number of best paths: {len(best_paths)}")
# print("Final best paths:")
# for x in best_paths:
#     print(x)

unique_pos = set([x for arr in best_paths for x in arr])
print(f"Number of unique positions to sit in: {len(unique_pos)}")

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i,j) in unique_pos:
            grid[i][j]='O'

# print("Final grid:")
# for x in grid:
#     print(''.join(x))
