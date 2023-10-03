import sys, heapq

n = int(input())
room = []
endtime = []
for i in range(n):
    room.append(list(map(int, input().split())))

room.sort(key = lambda x : (x[0], x[1]))
heapq.heappush(endtime, room[0][1])

for i in range(1, n):
    temp = heapq.heappop(endtime)
    if temp <= room[i][0]:
        heapq.heappush(endtime, room[i][1])
    else:
        heapq.heappush(endtime, temp)
        heapq.heappush(endtime, room[i][1])

print(len(endtime))