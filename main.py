import numpy as np

## 0's denote an empty cell

## Grid 1
##grid = [[0,1,0,2,3,0,0,4,0],
##        [0,0,0,4,0,5,6,0,0],
##        [7,0,4,0,0,8,0,2,3],
##        [0,0,5,0,0,9,0,0,0],
##        [3,0,8,0,0,0,9,0,7],
##        [0,0,0,6,0,0,8,0,0],
##        [5,3,0,7,0,0,4,0,1],
##        [0,0,9,5,0,1,0,0,0],
##        [0,6,0,0,8,2,0,9,0]]

## Grid 2
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def allowed(r, c, n):
    '''Determine if a number is allowed in a cell or not'''
    # Check each row
    for i in range(9):
        if grid[r][i] == n:
            return False
        
    # Check each column
    for i in range(9):
        if grid[i][c] == n:
            return False
        
    # Check each 3x3 box
    r_box = r // 3 * 3
    c_box = c // 3 * 3
    for i in range(3):
        for j in range(3):
            if grid[r_box + i][c_box + j] == n:
                return False
    return True


def solve():
    '''Use recursion to try every number in every empty cell'''
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                # Try every number 1-9 to see if they are possible
                for n in range(1, 10):
                    # If so, make that cell that number
                    if allowed(r, c, n):
                        grid[r][c] = n
                        # Recursively call the solve() function to check the next cell
                        solve()
                        # If all 9 values are disallowed, the return statement will exit the function
                        # In that case, set the cell to 0 since that number led to a dead end
                        grid[r][c] = 0
                        # Try again for the next number in the (1, 10) loop
                return


# Run the program
print("Original: ")
print(np.matrix(grid), '\n')
solve()
print("Solved: ")
print(np.matrix(grid))


