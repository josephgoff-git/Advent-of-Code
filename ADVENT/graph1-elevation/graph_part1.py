f = open("data.txt", "r")
data = f.read()
print(data)

lines = data.strip().split('\n')

heights = {}
start_pos = None
end_pos = None
for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == 'S':
      start_pos = (i, j)
      heights[i, j] = 1
    elif lines[i][j] == 'E':
      end_pos = (i, j)
      heights[i, j] = 26
    else:
      heights[i, j] = ord(lines[i][j]) - ord('a') + 1

graph = {}
for i in range(len(lines)):
  for j in range(len(lines[i])):
    graph[i, j] = []
    if i > 0 and heights[i - 1, j] <= heights[i, j] + 1:
      graph[i, j].append((i - 1, j))
    if i < len(lines) - 1 and heights[i + 1, j] <= heights[i, j] + 1:
      graph[i, j].append((i + 1, j))
    if j > 0 and heights[i, j - 1] <= heights[i, j] + 1:
      graph[i, j].append((i, j - 1))
    if j < len(lines[i]) - 1 and heights[i, j + 1] <= heights[i, j] + 1:
      graph[i, j].append((i, j + 1))

def bfs(graph, start, end):
    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        if current == end: 
            return len(path)
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                # path = path.append(neighbor)
                queue.append((neighbor, path + [neighbor]))

# Assuming start_pos and end_pos are defined
shortest_path = bfs(graph, start_pos, end_pos)
print("Shortest Path:", shortest_path)