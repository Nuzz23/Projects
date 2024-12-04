import numpy as np
SEARCH_STR = 'XMAS'
LEN_SEARCH_STR = len(SEARCH_STR)

with open('./AdventOfCoding2024/Day4/data.txt', 'r', encoding='UTF-8') as fp:
    data = np.array([list(item.strip()) for item in fp])

def countWords(data:list[str], i:int, j:int)->int:
    somma = 0
    
    # Directions to check: horizontal, vertical, and diagonal directions
    directions = [
        [0, 1],  # right
        [0, -1], # left
        [1, 0],  # down
        [-1, 0], # up
        [1, -1], # down-left diagonal
        [1, 1],  # down-right diagonal
        [-1, -1], # up-left diagonal
        [-1, 1],  # up-right diagonal
    ]

    for dx, dy in directions:
        try:
            word = ''
            # Check in the current direction (dx, dy)
            for k in range(LEN_SEARCH_STR):
                ni, nj = i + dx * k, j + dy * k
                if ni < 0 or ni >= len(data) or nj < 0 or nj >= len(data[0]):
                    raise IndexError  # Out of bounds check
                word += data[ni][nj]

            if word == SEARCH_STR:
                somma += 1

        except IndexError:
            pass  # Ignore out-of-bound errors

    return somma
    

somma = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'X':
            somma += countWords(data,i , j)

print(somma)

# Function to check if the "X-MAS" shape exists with center (i, j)
def count_XMAS(data: np.ndarray, i: int, j: int) -> int:
    try:
        if  (data[i-1, j-1] == data[i-1, j+1] == 'M' and data[i+1, j-1] == data[i+1, j+1] == 'S') or \
            (data[i-1, j-1] == data[i+1, j-1] == 'M' and data[i-1, j+1] == data[i+1, j+1] == 'S' ) or \
            (data[i+1, j-1] == data[i+1, j+1] == 'M' and data[i-1, j-1] == data[i-1, j+1] == 'S') or \
            (data[i+1, j+1] == data[i-1, j+1] == 'M' and data[i-1, j-1] == data[i+1, j-1] == 'S' ):
            return 1    
    except IndexError:
        return 0

# Iterate through the grid and count all X-MAS shapes
somma = 0
for i in range(1, len(data) - 1):  # Start from 1 to len(data) - 1 to avoid out of bounds
    for j in range(1, len(data[i]) - 1):  # Same for columns
        if data[i][j] == 'A':  # We need 'A' in the center of X-MAS
            somma += count_XMAS(data, i, j)

print(somma)
