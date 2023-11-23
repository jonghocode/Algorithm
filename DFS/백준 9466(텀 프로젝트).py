# 처음에 문제를 풀 때 1~n까지 사이클이 된 부분만 제외하고 모든 부분을
# 탐색하니 시간초과가 났다. 그래서 처음부터 끝까지 싸이클이 아니더라도
# 그 안에서 작은 싸이클이 생길 수 있으므로 그것을 체크하면서 답 체크를
# 하니까 시간초과에 걸리지 않았다.

import sys
sys.setrecursionlimit(10**7)

def dfs(st, now):
    global flag, answer
    
    visit[now] = 1
    temp.append(now)

    if visit[lst[now]]: # 이미 한 번 방문했던 곳이면(싸이클이 있음)
        if lst[now] in temp: # 싸이클이 시작되는 부분부터 탐색
            cnt = 0
            for i in range(len(temp)):
                if temp[i] == lst[now]:
                    cnt += 1
                if 0 < cnt and cnt < 2: # 사이클을 답 체크
                    answer+=1
    else:
        dfs(st, lst[now])
    

T = int(input())
for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    lst = [lst[i]-1 for i in range(n)]
    answer = 0

    visit = [0 for _ in range(n)]
    for i in range(n):
        if visit[i] == 0:
            temp = []
            dfs(i, i)
            
                

    print(n - answer)