from collections import deque

n, w, l = map(int, input().split())
car = list(map(int, input().split()))
q = deque()

# w끝부분에 다 맞춰서 놔두기
# 

answer, sum, cnt, idx = 0, 0, 0, 0
while True:
    if idx < n and sum+car[idx] <= l and cnt < w:
        for i in range(len(q)):
            q[i][1] += 1
        q.append([car[idx], 1])
        sum += car[idx]
        idx += 1
        cnt += 1
    else:
        if len(q) == 0:
            break
        if q[0][1] >= w:
            x, y = q.popleft()
            sum -= x
            cnt -= 1
        for i in range(len(q)):
            q[i][1] += 1
        if idx < n and sum+car[idx] <= l and cnt < w:
            q.append([car[idx], 1])
            sum += car[idx]
            idx += 1
            cnt += 1
    answer += 1
    # print(f"answer : {answer}, q : {q}, sum : {sum}, cnt : {cnt}, idx : {q[0][1], w}")
print(answer)