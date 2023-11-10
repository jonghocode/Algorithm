# 승, 패 합쳐서 n-1개면 순위 결정 가능
# 단방향 그래프를 그리는데 자신이 받는 거와 자신에서 나가는게 합쳐서 n-1개면 가능
from collections import deque
def solution(n, results):
    answer = 0
    graph = {i : [] for i in range(1, n+1)} # 가는 그래프
    graph2 = {i : [] for i in range(1, n+1)} # 받는 그래프
    for a, b in results:
        graph[b].append(a)
        graph2[a].append(b)

    re = [0]*(n+1)
    for i in range(1, n+1):
        q = deque()
        q.append(i)
        chk = [0]*(n+1)
        chk[i] = 1
        cnt = 0
        while q:
            x = q.popleft()
            for k in range(len(graph2[x])):
                if chk[graph2[x][k]] == 0:
                    q.append(graph2[x][k])
                    chk[graph2[x][k]] = 1
                    re[i] += 1
    
                    
    go = [0]*(n+1)      
    for i in range(1, n+1):
        q = deque()
        q.append(i)
        chk = [0]*(n+1)
        chk[i] = 1
        cnt = 0
        while q:
            x = q.popleft()
            for k in range(len(graph[x])):
                if chk[graph[x][k]] == 0:
                    q.append(graph[x][k])
                    chk[graph[x][k]] = 1
                    go[i] += 1
    
    for i in range(1, n+1):
        if go[i] + re[i] == n-1:
            answer += 1
        
    return answer
