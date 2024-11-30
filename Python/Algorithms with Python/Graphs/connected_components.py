def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(el) for el in line.split()]
    graph.append(children)

visited = [False] * nodes

for node in range(nodes):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    split_comp = ' '.join([str(c) for c in component])
    print(f'Connected component: {split_comp}')