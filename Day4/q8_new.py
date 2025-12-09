# Check for MAS x MAS

ans = 0
with open("input.txt", "r") as f:
    grid = [x.strip() for x in f.readlines()]

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "A":
                # Check around this

                if (
                    1 <= i < len(grid) - 1
                    and 1 <= j < len(grid[0]) - 1
                    and (
                        grid[i - 1][j - 1] == "M"
                        and grid[i + 1][j + 1] == "S"
                        or grid[i - 1][j - 1] == "S"
                        and grid[i + 1][j + 1] == "M"
                    )
                    and (
                        grid[i - 1][j + 1] == "M"
                        and grid[i + 1][j - 1] == "S"
                        or grid[i - 1][j + 1] == "S"
                        and grid[i + 1][j - 1] == "M"
                    )
                ):
                    ans += 1

    print("ANSWER:", ans)
