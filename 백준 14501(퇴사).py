def check(x, y): # 스케줄이 있는지 확인
    for i in range(x, y+1):
        if chk[i] == 1:
            return 0
    return 1

def dfs(d, sum):
    global n, answer
    # d == n-1이라면 끝 넘어가면 안됨
    # 확인
    answer = max(answer, sum)

    for i in range(d, n):
        if i + schedule[i][0]-1 < n and check(i, i + schedule[i][0]-1): # 1일이면 0
            for j in range(i, i + schedule[i][0]):
                chk[j] = 1
            dfs(i, sum + schedule[i][1])
            for j in range(i, i + schedule[i][0]):
                chk[j] = 0

n = int(input())

answer = -1
schedule = []
chk = [0]*30

for i in range(n):
    schedule.append(list(map(int, input().split())))

dfs(0, 0)
print(answer)