from collections import deque
import copy


def bfs(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    count = 1

    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1
    return count


def solution(n, wires):
    answer = 9999999

    for i in range(len(wires)):
        wires_copy = copy.deepcopy(wires)
        wires_copy.pop(i)
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        for v1, v2 in wires_copy:
            graph[v1].append(v2)
            graph[v2].append(v1)

        answer = min(abs(2 * bfs(1, graph, visited) - n), answer)

    return answer