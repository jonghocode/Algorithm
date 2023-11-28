# 처음가지고 있는 열쇠를 가지고 들어갈 수 있는 방향의 좌표를 리스트에 먼저 넣기
# 들어갈 수 있는 모든 방향으로 들어가서 열쇠 먼저 줍기(chk되어 있으면 한번 더 방문 X)

# 이제 또 가지고 있는 열쇠를 가지고 들어갈 수 있는 방향의 좌표를 리스트에 먼저 넣기
# 들어갈 수 있는 모든 방향으로 들어가서 문서 줍기(chk되어 있으면 한번 더 방문 X)
# !! 처음 문제를 풀 때 이런 알고리즘으로 풀려고 했다. 하지만 이렇게 푸니까 나중에 열쇠를 가질 수 있는 경우가 생겨서 코드가 너무 복잡해지고 반례도 많이 생겨서
# 알고리즘을 변경했다.
# ------------------------------------------------------------------------------
# 그것은 열쇠를 찾으면 방문 배열을 초기화 하고 다시 돌아다닌다! 이렇게 되면 열쇠가 새로 생길 때 마다 새로운 곳을 더 가볼 수 있기 때문에 모든 곳을 탐색할 수 있고
# 코드도 간단해진다.

from collections import deque

dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    board = ['.' + input() + '.' for _ in range(n)]
    board = ['.' * (m+2)] + board + ['.' * (m+2)] # 배열 크기를 늘려서 처음 시작부분을 0,0으로 고정시킨다.
    visit = [[0 for _ in range(m+2)] for _ in range(n+2)]
    key = list(input())
    answer = 0
    dict = {} # 키 저장

    for i in key:
        if i != '0':
            dict[i] = 1

    q = deque([])
    q.append([0, 0])
    visit[0][0] = 1
    document = []

    while q:
        x, y= q.popleft()
        for i in range(4):
            nx, ny = x + dirx[i], y + diry[i]
            if nx < 0 or nx >= n+2 or ny < 0 or ny >= m+2 or board[nx][ny] == '*' or visit[nx][ny] == 1:
                continue
            if 'A' <= board[nx][ny] <= 'Z' and board[nx][ny].lower() not in dict: # 키가 없으면 continue
                continue
            elif 'a' <= board[nx][ny] <= 'z':
                if board[nx][ny] not in dict: # 키를 새로 주우면 방문배열 초기화
                    dict[board[nx][ny]] = 1
                    visit = [[0 for _ in range(m+2)] for _ in range(n+2)]
            elif board[nx][ny] == '$' and (nx, ny) not in document:
                document.append((nx, ny))
                answer += 1
            visit[nx][ny] = 1
            q.append([nx, ny])
    print(answer)
