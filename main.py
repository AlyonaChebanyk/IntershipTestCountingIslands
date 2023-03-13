import numpy as np


def count_islands(matrix):
    matrix = np.array(matrix)
    n, m = matrix.shape
    count = 0

    def find_island(i, j):
        if i < 0 or i == n or j < 0 or j == m:
            return
        elif matrix[i, j] == 1:
            matrix[i][j] = -1

            find_island(i+1, j)
            find_island(i-1, j)
            find_island(i, j+1)
            find_island(i, j-1)
        else:
            return

    for i in np.arange(n):
        for j in np.arange(m):
            if matrix[i][j] == 1:
                count += 1
                find_island(i, j)

    return count


if __name__ == '__main__':
    matrix = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1]
    ]
    print("Matrix 1")
    print(np.array_str(np.array(matrix)))
    print(f"Islands: {count_islands(matrix)}")

    matrix = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0]
    ]
    print("\nMatrix 2")
    print(np.array_str(np.array(matrix)))
    print(f"Islands: {count_islands(matrix)}")

    matrix = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1]
    ]
    print("\nMatrix 3")
    print(np.array_str(np.array(matrix)))
    print(f"Islands: {count_islands(matrix)}")
