grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

textgrid = ""
for i in range(len(grid)):
    for j in range(len(grid[i])):
        textgrid += grid[i][j]
    textgrid += "\n"
lines = textgrid.strip().split('\n')

# Create an object of integers
pieces = {}
for i in range(len(lines)):
  for j in range(len(lines[i])):
    pieces[i,j] = int(lines[i][j])

graph = {}
for i in range(len(lines)):
  for j in range(len(lines[i])):
    if pieces[i,j] == 1:
        graph[i, j] = []
        if i > 0 and pieces[i - 1, j] == 1:
            graph[i, j].append((i - 1, j))
        if i < len(lines) - 1 and pieces[i + 1, j] == 1:
            graph[i, j].append((i + 1, j))
        if j > 0 and pieces[i, j - 1] == 1:
            graph[i, j].append((i, j - 1))
        if j < len(lines[i]) - 1 and pieces[i, j + 1] == 1:
            graph[i, j].append((i, j + 1))

def bfs_helper(graph):
    start = list(graph.keys())[0]
    queue = [start]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                queue.append(neighbor)
    
    return visited

def bfs(graph):
    islands = 0

    while graph: 
        visited = bfs_helper(graph)
        islands += 1
        for item in visited:
            graph.pop(item)

    return islands
