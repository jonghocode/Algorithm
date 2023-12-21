import sys
sys.setrecursionlimit(10**4)
def dfs(now, color):
    visit[now] = color # 현재 색깔 넣기
    for go in graph[now]:
        if visit[go] == -1: # 방문하지 않았다면
            next = 1 if color == 0 else 0 # 색깔 바꾸기
            res = dfs(go, next)
            if not res: # 재귀적으로 수행하므로 return 되어서 돌아온 값이 false면 바로 false를 반환해야 함
                return False
        elif visit[go] == color:
            return False
    return True

t = int(input())
for _ in range(t):
    node, edge = map(int, input().split())
    graph = {i : [] for i in range(1, node+1)}
    visit = [-1 for _ in range(node+1)]

    for _ in range(edge):
        st, ed = map(int, input().split())
        graph[st].append(ed)
        graph[ed].append(st)
    
    for i in range(1, node+1):
        if visit[i] == -1 and i in graph:
            answer = dfs(i, 0)
            if not answer: # false면 break
                break
    print("NO") if not answer else print("YES")