import sys

def find(idx): # 부모 찾기
    if root[idx] == idx:
        return root[idx]
    root[idx] = find(root[idx])
    return root[idx]

def dfs(idx, type): # 원수의 원수는 친구이기 때문에 이분그래프 처럼 나누기
    if visit[idx] != 0:
        return
    visit[idx] = type
    type *= -1
    for v in graph[idx]:
        if visit[v] == 0:
            dfs(v, type)

n = int(input())
m = int(input())
root = [i for i in range(n+1)]
graph = {i : [] for i in range(1, n+1)} # 원수 그래프 생성

for _ in range(m):
    lst = list(map(str, sys.stdin.readline().strip().split()))
    k, a, b = lst[0], int(lst[1]), int(lst[2])
    if k == 'F': # 친구라면 바로 묶어주기
        n1, n2 = find(a), find(b)
        if n1 != n2:
            root[n2] = n1
    else:
        graph[a].append(b)
        graph[b].append(a)

visit = [0 for i in range(n+1)]
cnt = -1
for i in range(1, n+1):
    if visit[i] == 0 and len(graph[i]): # 원수 그래프 만들기
        dfs(i, cnt)
        cnt -= 1

chk = [0 for i in range(n+1)]
for i in range(1, n+1): # 친구 그래프와 합쳐주기
    if visit[i] == 0 or chk[i] == 1: continue
    for j in range(n+1):
        if visit[i] == visit[j] and chk[j] == 0:
            n1, n2 = find(i), find(j)
            if n1 != n2:
                root[n2] = n1
            chk[i] = 1; chk[j] = 1

answer = set()
for i in range(1, n+1):
    answer.add(find(i))
print(len(answer))