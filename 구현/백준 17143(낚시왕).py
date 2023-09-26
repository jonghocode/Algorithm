# map은 1,1부터 시작, 사람은 0,0에서 시작
# 1. 사람이 오른쪽 한 칸 이동
# 2. y값이 같고 x가 가장 작은 것을 잡고 없애기
# 3. 상어 이동(가장 크기가 큰 상어가 다 먹음)
# d : 1/북, 2/남, 3/동, 4/서

# 답 : 사람이 잡은 상어 크기의 합

# 상어 이동 : 현재 방향에서 벽 쪽으로 다 이동 후 벽 옆으로 이동했고 이동할 수 있는 칸이 남았으면 방향 바꾸기 / 아니라면 방향 바꾸지 않기
# 남은 칸 수 // (열 개수-1) -> 홀수면 방향 그대로 짝수면 방향 바꾸기
# 현재 방향에서 남은 칸 수 % (열개수-1) 만큼 앞으로 이동
# 상어 리스트에 바뀐 것을 다 넣기 -> 같은 x,y좌표가 있다면 크기가 제일 큰 놈 만 남겨놓기
# 사람위치가 y+1이 되면 반복 종료

zx, zy = [0, -1, 1, 0, 0], [0, 0, 0, 1, -1]
r, c, m = map(int, input().split())
shark = []
answer = 0

if m != 0:
    for i in range(m):
        shark.append(list(map(int, input().split())))
        # x, y, s, d, z
        #       속 방 크

    def move(x, y, s, d, z):
         # 열로 움직일 때 행으로 움직일 때 따로 처리
        t = s
        if d == 1:
            if t >= x-1:
                t -=(x-1)
                x = 1
                d = 2
                
            else:
                x = x-t
                t = 0
        elif d == 2:
            if t >= r-x:
                t -= (r-x)
                x = r
                d = 1
                
            else:
                x = x+t
                t = 0
        elif d == 3:
            if t >= c-y:
                t -=(c-y)
                y = c
                d = 4
            else:
                y = y+t
                t = 0
        elif d == 4:
            if t >= y-1:
                t -= (y-1)
                y = 1
                d = 3
            
            else:
                y = y-t
                t = 0
        # print(t)
        return [x,y,t,d,z]
        

    # 1. 오른쪽으로 한 칸 이동
    for i in range(1, c+1):
    
        shark.sort(key = lambda x : (x[1], x[0]))

        for j in range(len(shark)):
            if shark[j][1] == i:
                answer += shark[j][4]
                shark.pop(j) # 2. 잡고 빼기
                break
        
        ttt = 0
        lst = []
        # 상어 이동
        while shark:
            x, y, s, d, z = shark.pop(0)
            temp = s
            mod = move(x, y, s, d, z) # 처음 벽 쪽으로 이동
            # print("%d"%i, mod)
            # 나머지로 계산 후 좌표 바꾸기
            # 홀수면 현재 반대편에 놔두고 방향 바꾸기
            # 짝수면 그대로
            if mod[3] == 1 or mod[3] == 2 and mod[2] != 0: # 북, 남
                if mod[2] >= r-1 and (mod[2] // (r-1)) % 2 != 0: # 홀수면 바꾸기
                    if mod[0] == 1:
                        mod[0] = r
                        mod[3] = 1
                    elif mod[0] == r :
                        mod[0] = 1
                        mod[3] = 2
                    
                k = mod[2] % (r-1)
                if mod[3] == 1:
                    mod[0] -= k
                else:
                    mod[0] += k

                
            elif mod[3] == 3 or mod[3] == 4 and mod[2] != 0:
                if mod[2] >= c-1 and (mod[2] // (c-1)) % 2 != 0:
                    if mod[1] == 1:
                        mod[1] = c
                        mod[3] = 4
                    elif mod[1] == c :
                        mod[1] = 1
                        mod[3] = 3
                    
                k = mod[2] % (c-1)
                if mod[3] == 3:
                    mod[1] += k
                else:
                    mod[1] -= k
            # lst에 넣기
            lst.append([mod[0], mod[1], temp, mod[3], mod[4]])
            ttt = 1
        # lst정렬 후 x, y가 겹치면 다 빼기
        # print(lst)
        if ttt == 1:
            lst.sort(key = lambda x : (x[0], x[1], -x[4]))
            shark.clear()
            chk = [[0]*101 for _ in range(101)]
            for i in range(len(lst)):
                if chk[lst[i][0]][lst[i][1]] == 0:
                    chk[lst[i][0]][lst[i][1]] = 1
                    shark.append([lst[i][0], lst[i][1], lst[i][2], lst[i][3], lst[i][4]])
        
print(answer)