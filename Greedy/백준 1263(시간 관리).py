# 시간복잡도 : 1000 = n

n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))

# 최대한 늦은 시간 을 기준으로 내림차순
# why ? 그 순간에 가장 최적의 답을 고르기 위해 어떻게 할까 생각하다가
# 가장 늦은 시간부터 순서대로 시간을 빼는게 가장 최적의 답이라는 결론이 나왔다.
time.sort(key = lambda x : (-x[1], -x[0]))

st = time[0][1] - time[0][0] # 처음 기준 값을 정함
for i in range(1, len(time)):
    if st > time[i][1]: # 그 다음에 일을 해야할 시간이 더 작기 때문에 일관성 있게 최적을 구하기 위해서 새로 기준 바꾸기 
        st = time[i][1] - time[i][0]
    else: # 현재 시간이 더 작은 것은 그 전까지 최적의 답을 골랐기 때문에 그대로 빼주기
        st -= time[i][0]

if st < 0:
    st = -1
print(st)