# # 갈 수 있는 곳 중에서 가장 큰 값 빼기
# # 최대힙(두개의 합, 현재 위치, 남은 연료)

# # 두개의 합 보다 lst[i][0]이 작은 것을 다 넣는다
# # 넣을 때는 저 두개의 합, lst[i][1], 두개의합 - lst[i][1]
# # 이렇게해서 힙에서 뺀 개수를 구하면 답
# import heapq, sys

# n = int(input())
# station = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
# station.sort()
# ex, oil = map(int, input().split())
# idx = 0 # for문 idx
# answer = 0
# prior = 0
# st = oil

# while True:
#     if st >= ex:
#         break
#     sw = 0
#     heap = []
#     for i in range(idx, n):
#         if station[i][0] <= st:
#             two = station[i][0]
#             three = oil - (station[i][0] - prior) + station[i][1]
#             heapq.heappush(heap, [-(two + three), -two, -three])
#             sw = 1
#         else:
#             idx = i
#             break
#     print(heap, idx)
#     if sw == 0:
#         print(-1)
#         exit()
#     else:
#         lst = heapq.heappop(heap)
#         print(lst)
#         st = -lst[0]
#         prior = -lst[1]
#         oil = -lst[2]
#     answer += 1
# print(answer)

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
oil_list = [list(map(int, input().split())) for _ in range(N)]
oil_list.sort( key = lambda x : (x[0], -x[1]))
L, P = map(int, input().split())
oil_list.append([L, 0])
oil_heap = list()
cnt = 0

for l, p in oil_list :
  print(l, p)
  if P >= L :
    break
  while P < l and oil_heap :
    P += -heappop(oil_heap)
    cnt += 1
    print(f"pop / P : {P}, oil_heap : {oil_heap}")
  if P < l :
    break
  heappush(oil_heap, -p)
  print(f"push : {oil_heap}")

print(cnt if P >= L else -1)