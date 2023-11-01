import sys
from collections import deque

n, m, x = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
for i in range(m): # 그래프 만들기
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([b, c])


# 1 -> 2 보다 1 -> 4 -> 2 로 가는게 더 빠를 수도 있음
answer = [] # 마지막에 한꺼번에 비교하기 위해서 정답 리스트
for i in range(1, n+1): # 각 마을에서 모든 마을을 가는데 필요한 최단 시간 기록
    visit = [0x7fffffff for _ in range(n+1)]
    q = deque([])
    q.append([i, 0]) # 시작점 기록

    while q:
        num, money = q.popleft() # 현재 마을, 비용

        if visit[num] < money: # 현재 마을에 기록된 값보다 비용이 더 높으면 
            continue  

        for i in range(len(graph[num])): # 현재 마을과 연결되어 있는 곳
            end, cost = graph[num][i][0], graph[num][i][1] # 도착점, 비용
            if visit[end] >= money + cost: # 기록되어 있는 값 보다 더 작으면 넣기
                visit[end] = money + cost
                q.append([end, money + cost])

    answer.append(visit)

ans = -1 # 최댓값을 구하기 위한 변수
for i in range(1, n+1):
    if i == x: continue # 파티가 열리는 마을이면 continue
    ans = max(ans, answer[i-1][x] + answer[x-1][i]) # 파티하는 마을까지 비용 + 돌아오는 비용
print(ans)