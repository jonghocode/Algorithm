def dfs(now, color):
    global sw

    visit[now] = color
    for go in graph[now]:
        if visit[go] == -1:
            next = 1 if color == 0 else 0
            dfs(go, next)
        elif visit[go] == color:
            sw = 1
            return

t = int(input())
for _ in range(t):
    node, edge = map(int, input().split())
    graph = {i : [] for i in range(1, node+1)}
    visit = [-1 for _ in range(node+1)]

    for _ in range(edge):
        st, ed = map(int, input().split())
        graph[st].append(ed)
        graph[ed].append(st)
    
    sw = 0
    for i in range(1, node+1):
        if visit[i] == -1 and i in graph:
            dfs(i, 0)
            if sw == 1:
                print("NO")
                break
    
    if sw == 0:
        print("YES")
    