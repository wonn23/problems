from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    visited = [False] * len(words)
        
    q = deque()
    q.append((begin, 0))
    
    while q:
        node, depth = q.popleft()
        
        if node == target:
            return depth
        
        for i in range(len(words)):
            if sum([a!=b for a,b in zip(node,words[i])]) == 1: # 한 글자만 다른 경우
                if not visited[i]: # 아직 방문하지 않았다면
                    visited[i] = True # 방문 표시를 하고
                    q.append((words[i], depth+1)) # 큐에 추가한다.
                
    return 0
