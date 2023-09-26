# 앞에서 부터 뒤에것만 보면서 바꾸면서 가는게 그 상황에서 제일 좋은 방법
# 맨 처음 것을 누르냐 안누르냐(예외처리 왜냐하면 첫 번째 버튼은 2개만 바뀌기 때문)
n = int(input())
st = list(map(int, input()))
ed = list(map(int, input()))
t = st[:]

def search(start, end, cnt):
    for i in range(1, len(start)):
        if start[i-1] != end[i-1]:
            cnt += 1
            for j in range(i-1, i+2):
                if j<len(start):
                    if start[j] == 0:
                        start[j] = 1
                    else:
                        start[j] = 0
   
    if start == end:
        return cnt
    else:
        return 987654321
    
answer = search(st, ed,0)
if t[0] == 0:
    t[0] = 1
else:
    t[0] = 0
if t[1] == 0:
    t[1] = 1
else:
    t[1] = 0
answer = min(answer,search(t,ed,1))
if answer == 987654321:
    answer = -1
print(answer)
