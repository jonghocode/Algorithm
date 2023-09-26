from collections import deque

find = int(input())
n = int(input())
lst = []
if n != 0:
    lst= list(map(int, input().split()))

q = deque([])
q.append([100, 0, 0])
chk = [[0]*2 for _ in range(1000030)]

while q:
    now, d, sw = q.popleft()

    if now == find:
        print(d)
        break
    if chk[now][sw] == 1: # 큐에서 뺀 값이 이미 체크가 되어 있으면 더 이상 할 필요 없음
        continue
    chk[now][sw] = 1 # 뺀 값 체크
    
    if sw == 1 or now == 100: # 이 부분을 안 넣어주니까 메모리 초과 남
        for i in range(10):
            if i not in lst:
                if sw == 0: # 처음 들어온 경우는 숫자만 저장
                        q.append([i, d+1, 1])
                else:
                    if now*10+i <= 1000011: # 만약 눌려졌었다면 숫자 덮어쓰기
                        q.append([now*10+i, d+1, 1])
                    
            
    
    if now+1 <= 1000011:
        q.append([now+1, d+1, 0])

    if now-1 >= 0 :
        q.append([now-1, d+1, 0])

