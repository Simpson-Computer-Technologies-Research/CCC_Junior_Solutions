

# // Get the pool size and the number of
# // trees to add to the grid
pool_size: int = int(input("pool size: "))
number_of_trees: int = int(input("trees: "))


# // Establish grid variables
grid: list[list[int]] = []
res: list[list[int]] = []

# // Create a new grid
for _ in range(pool_size):
    grid.append([0 for _ in range(pool_size)])

# // Add the trees to the grid
for _ in range(number_of_trees):
    x_y: str = input("")
    x: int = int(x_y.split(" ")[0])
    y: int = int(x_y.split(" ")[1])
    grid[x][y] = 1


# // Check the pool y indices for 1's
def check_pool_y(row: int, i: int):
    for p in range(pool_size):
        if 1 in grid[p+row]:
            break

        q = grid[p+row][i:i+pool_size]
        if 1 not in q:
            res.append(q)

# // Iterate over the x arrays of the grid
for row in range(len(grid)):
    for i in range(len(grid)):

        # // Required or else error
        if i + pool_size > len(grid[row]):
            break
        
        # // Check the pool y values
        if 1 not in grid[row][i:i+pool_size]:
            check_pool_y(row, i)


# // Establish variables
temp: int = 0
block_length: int = 0

# // Iterate over the result
for i in res:
    temp += 1
    block_length = len(i)

    # // Break if block_length is equal to temp
    if temp == block_length:
        print(block_length)
        break


