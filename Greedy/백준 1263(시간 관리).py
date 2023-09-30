# 최대한 늦은 시간 을 기준으로 내림차순

n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))

time.sort(key = lambda x : (-x[1], -x[0]))
st = time[0][1] - time[0][0]
for i in range(1, len(time)):
    if st > time[i][1]:
        st = time[i][1] - time[i][0]
    else:
        st -= time[i][0]
        
if st < 0:
    st = -1
print(st)