import sys, heapq

n = int(input())
room = []
endtime = []
for i in range(n):
    room.append(list(map(int, input().split())))

# 시작시간을 기준으로 오름차순 정렬(처음에는 끝나는 시간을 기준으로 오름차순 했다가 반례가 생겨서 정렬기준을 바꿨다.)
room.sort(key = lambda x : (x[0], x[1]))
heapq.heappush(endtime, room[0][1])
# 처음에는 heap을 쓰지않고 정렬로만 하려고 했지만 heap을 쓰는게 시간이 훨씬 줄어들고
# 관리하기도 편하기 때문에 heap을 쓴다

for i in range(1, n):
    # 끝나는 시간이 가장 빠른 것부터 뺀다
    temp = heapq.heappop(endtime)
    if temp <= room[i][0]: # 현재의 시작시간보다 가장 빠르게 끝나는 시간이 더 작거나 같으면 그거를 수정해서 씀
        heapq.heappush(endtime, room[i][1])
    else: # 새로운 강의실 넣기
        heapq.heappush(endtime, temp)
        heapq.heappush(endtime, room[i][1])

print(len(endtime))