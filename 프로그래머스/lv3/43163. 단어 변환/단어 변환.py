from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0 # words 리스트에 target이 없을 때
    
    visited = [False] * len(words)
        
    q = deque()
    q.append((begin, 0))
    
    while q:
        node, depth = q.popleft()
        
        if node == target:
            return depth
        
        for i in range(len(words)):
            if not visited[i] and sum(a!=b for a,b in zip(node,words[i])) == 1:
                    visited[i] = True
                    q.append((words[i], depth+1))