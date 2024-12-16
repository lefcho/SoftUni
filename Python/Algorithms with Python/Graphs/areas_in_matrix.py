def dfs(row, col, matrix, visited, parent_key):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if matrix[row][col] != parent_key:
        return

    if visited[row][col]:
        return

    visited[row][col] = True

    dfs(row - 1, col, matrix, visited, parent_key)
    dfs(row + 1, col, matrix, visited, parent_key)
    dfs(row, col - 1, matrix, visited, parent_key)
    dfs(row, col + 1, matrix, visited, parent_key)


rows = int(input())
cols = int(input())

matrix = []
visited = []

for i in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}
areas_count = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue

        key = matrix[row][col]
        dfs(row, col, matrix, visited, key)

        areas_count += 1
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1

print(f'Areas: {areas_count}')

for key, value in sorted(areas.items()):
    print(f"Letter '{key}' -> {value}")
