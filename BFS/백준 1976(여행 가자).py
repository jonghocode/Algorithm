import sys
from collections import deque

n = int(input())
m = int(input())
graph = {i : [] for i in range(n)}

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(len(lst)): # 그래프 만들기
        if lst[j] == 1:
            graph[i].append(j)

command = list(map(int, input().split()))

def bfs(start, end): # 지금 위치에서 다음 위치를 갈 수 있는지
    q = deque()
    chk = [0]*n
    q.append(start)
    chk[start] = 1

    while q:
        x = q.popleft()
        if x == end:
            return True
        for i in range(len(graph[x])):
            if chk[graph[x][i]] == 0:
                q.append(graph[x][i])
                chk[graph[x][i]] = 1

    return False

for i in range(m-1):
    if not bfs(command[i]-1, command[i+1]-1):
        print("NO")
        exit() # 문제를 풀 때 이 부분에 exit()를 넣어주지 않아서 계속 틀렸었다. no가 나왔을 때 프로그램 종료를 안하면 밑에 YES도 출력됨

print("YES")