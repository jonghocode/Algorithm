# pypy로 통과했음
# 이어진 동그라미 2개의 색깔이 달라야하기 때문에 방문을 하지 않았다면
# 현재 색깔과 다른 색깔을 넣어주고 방문을 했다면 현재 색깔과 비교했을 때
# 같다면 impossible로 출력한다.

import sys

def dfs(color, now):
    global sw
    for i in range(len(graph[now])):
        if visit[graph[now][i]] == -1:
            if color == 0:
                visit[graph[now][i]] = 1
                dfs(1, graph[now][i])
            else:
                visit[graph[now][i]] = 0
                dfs(0, graph[now][i])
        elif visit[graph[now][i]] == color: # 현재 색깔과 같다면 체크
            sw = 1
            return
        
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = {i : [] for i in range(1, n+1)}
    for _ in range(m):
        st, ed = map(int, input().split())
        graph[st].append(ed)
        graph[ed].append(st)
    
    sw = 0
    visit = [-1 for _ in range(n+1)]
    visit[st] = 0
    dfs(0, st)
    if sw == 0:
        print('possible')
    else:
        print('impossible')