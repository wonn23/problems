n, k = map(int,input().split())
graph = []
visited = [False for i in range(n)]
for i in range(n):
    graph.append([i,int(input())])
visited[0] = True
stack = []
count = 1
stack.append(graph[0][1])
while stack:
    v = stack.pop()
    if k == v:
        print(count)
        break
    elif visited[v] == False:
        visited[v] =True
        count += 1
        stack.append(graph[v][1])
    else:
        print(-1)
        break