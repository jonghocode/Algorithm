n, k = map(int, input().split())
schedule = list(map(int, input().split()))
chk = [0 for _ in range(101)]
for i in schedule:
    chk[i] += 1

answer, memory = 0, []

for i in range(len(schedule)):
    now = schedule[i]
    if now not in memory:
        if n > 0: # 콘센트 자리가 남았으면
            memory.append(now)
            n -= 1
        else:
            # 현재 메모리에 올라와 있는 것 중에서 뒤 스케줄에 더이상 나오지 않는다면 바로 뽑기
            flag = False
            for j in range(len(memory)):
                if chk[memory[j]] == 0:
                    memory.pop(j)
                    flag = True
                    break

            # 위 조건에 걸리지 않았다면 현재 메모리에 올라와 있는 것 중 앞으로 남은 스케줄 중 제일 늦게 나오는 것 뽑기
            if not flag:
                visit = [0 for _ in range(101)]
                for j in range(i+1, k):
                    if schedule[j] in memory and visit[schedule[j]] == 0:
                        visit[schedule[j]] = 1
                        idx = j
                for j in range(len(memory)):
                    if schedule[idx] == memory[j]:
                        memory.pop(j)
                        break
            answer += 1
            memory.append(now)
            
    chk[now] -= 1
    
print(answer)

# 3 14
# 1 4 3 2 5 4 3 2 5 3 4 2 3 4

# 3은 뒤에 2개가 있고 3번째 뒤에 나옴
# 4는 뒤에 2개가 있고 4번째 뒤에 나옴
# 5는 뒤에 1개가 있고 2번째 뒤에 나옴

# 1
# 4 3 2

# 2
# 4 3 5

# 3
# 3 5 2

# 4
# 2 3 4