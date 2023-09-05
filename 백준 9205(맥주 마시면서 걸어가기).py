# 1. 현재위치부터 락페스티벌 까지 갈 수 있는지 체크
# 2. 못 간다면 갈 수 있는 편의점 큐에 넣기
import sys
from collections import deque

def bfs(a, b, c, d, store):
    q = deque([])
    nowx, nowy = a, b
    q.append([nowx, nowy])
    chk = [0]*len(store)

    while q:
        x, y = q.popleft()
        if x == c and y == d:
            return 1
        for i in range(len(store)):
            if chk[i] == 0 and abs(store[i][0] - x) + abs(store[i][1] - y) <= 1000:
                chk[i] = 1
                q.append([store[i][0], store[i][1]])
    return 0

TEST = int(input())
for i in range(TEST):
    n = int(input())
    a, b = map(int, input().split())
    
    store = []
    for j in range(n+1):
        store.append(list(map(int, sys.stdin.readline().split())))

    if bfs(a, b, store[n][0], store[n][1], store):
        print("happy")
    else :
        print("sad")
