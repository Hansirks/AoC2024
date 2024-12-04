def preprocess_file_to_grid(file_path):
    """
    Reads input data from a file, splits it by newline characters, and preprocesses it into a grid format.
    """
    
    with open(file_path, 'r') as file:
        rows = file.read().strip().splitlines() 
    grid = [list(row) for row in rows]
    return grid


def count_xmas_occurrences(grid):
    """
    Counts occurrences of the word 'XMAS' in all directions in the given word search grid.
    """
    #To find 
    word = "XMAS"
    word_length = len(word)
    rows, cols = len(grid), len(grid[0])
    count = 0

    # All possible Directions??
    directions = [
        (0, 1),          # Right
        (0, -1),         # Left
        (1, 0),          # Down
        (-1, 0),         # Up
        (1, 1),          # Down-right
        (-1, -1),        # Up-left
        (1, -1),         # Down-left
        (-1, 1),         # Up-right
    ]
    
    # Finding Directions
    def search(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                return False
            if grid[nx][ny] != word[i]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search(i, j, dx, dy):
                    count += 1
    
    return count


file_path = "./D4/wordsearch.txt" 


grid = preprocess_file_to_grid(file_path)

#XMAS
result = count_xmas_occurrences(grid)

print(result)

#PART 2
def count_xmas_patterns(grid):
    """
    Counts occurrences of the X-MAS pattern in the given word search grid.
    """
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Possible MAS patterns 
    mas_variants = ["MAS", "SAM"]

    def is_xmas(x, y):
        # Check if X-MAS pattern fits within bounds
        if (
            x - 1 >= 0 and x + 1 < rows                         # Vertical 
            and y - 1 >= 0 and y + 1 < cols                     # Horizontal 
        ):
            # Find diagonals
            top_left = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1]
            top_right = grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1]

            # Match Patterns 
            if top_left in mas_variants and top_right in mas_variants:
                return True
        return False

    for i in range(rows):
        for j in range(cols):
            if is_xmas(i, j):
                count += 1

    return count


#X-MAS
result = count_xmas_patterns(grid)
print(result)