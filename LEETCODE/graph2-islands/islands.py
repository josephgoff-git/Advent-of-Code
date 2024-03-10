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

def bfs(graph):
    islands = 0
    mylist = list(graph)
    start = (0,0)
    done = False
    
    if len(mylist) > 0:
        start = mylist[0]
    else:
        done = True

    queue = [start]
    visited = set()

    while not done: 
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                for neighbor in graph[current]:
                    queue.append(neighbor)
        
        # Starting piece has no more connected land
        islands += 1

        # Delete visitied nodes from the graph
        for item in visited:
            graph.pop(item)
        visited = set()

        if len(list(graph)) == 0:
            done = True
        else: 
            # Restart the queue
            start = list(graph)[0]
            queue = [start]

    return islands

# Assuming start_pos and end_pos are defined