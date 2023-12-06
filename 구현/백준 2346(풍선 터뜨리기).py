# 백준 2346(풍선 터뜨리기)
# 1 ~ n 까지 번호에 다음 움직여야하는 값이 있음
# 첫번째는 무조건 1번 터뜨리기
# lst[1]로 가서 터뜨리고 값을 얻은 후 세칸 오른쪽이동(앞에꺼 빼서 뒤에 넣기)
# 다음 얻은값으로 이동
# -는 뒤에꺼 빼서 앞에 넣기

from collections import deque

n = int(input())
lst = list(map(int, input().split()))

st, answer = lst[0], [1]
q = deque()
for i in range(2, n+1):
    q.append(i)

while q:
    if st < 0: # 음수는 포함을 시키면 안되기 때문에 0
        while st != 0:
            now = q.pop()
            st += 1
            q.appendleft(now)
    else:
        while st != 1: # 양수는 하나 포함 시켜야하기 때문에 1
            now = q.popleft()
            st -= 1
            q.append(now)
    t = q.popleft()
    st = lst[t-1]
    answer.append(t)
print(' '.join(map(str, answer)))