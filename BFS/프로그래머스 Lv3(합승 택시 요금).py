from collections import deque

def solution(n, s, a, b, fares):

    def bfs(p):
        lst = [0x7fffffff for _ in range(n+1)]
        q = deque()
        q.append([p, 0])
        
        while q:
            now, cost = q.popleft()
            if lst[now] < cost: continue # 이 if문은 꼭 있어야함
            lst[now] = cost
            for i in range(len(graph[now])):
                end, money = graph[now][i][0], graph[now][i][1]
                if lst[end] > money + cost: # 더 크면 가지 않기
                    lst[end] = money + cost
                    q.append([end, money+cost])
        return lst
    
    
    answer = 0x7fffffff
    graph = {i : [] for i in range(1, n+1)}
    for x, y, z in fares:
        graph[x].append([y, z])
        graph[y].append([x, z])
        
    for i in range(1, (n+1)):
        lst = bfs(i) # 반환
        # print(lst)
        answer = min(answer, lst[s] + lst[a] + lst[b]) # 제일 작은 값 구하기
        
        
    return answer