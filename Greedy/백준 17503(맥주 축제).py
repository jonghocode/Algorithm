# 자바 과제!!!!!

# 도수를 넘지 않으면서 선호도 합이 M 이상
# 맥주를 모두 마실 수 있는 간레벨
# n, m, k
# 선호도, 도수레벨
import sys
from heapq import heappush, heappop

n, m, k = map(int, input().split())
beer = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
beer.sort(key = lambda x : (x[1], -x[0]))
answer = []
sum = 0

for fav, al in beer:
    if sum >= m and len(answer) == n:
        break
 
    if len(answer) == n:
        t = heappop(answer)
        sum -= t[0]
        heappush(answer, [fav, al])
        sum += fav
    else:
        heappush(answer, [fav, al])
        sum += fav

result = -1
if sum >= m:
    for i in answer:
        result = max(result, i[1])
print(result)
print(answer)
# 간레벨 먼저
# 정답배열을 선호도 최소 힙의 길이가 n이고 선호도가 다 안채워졌으면 정답배열에서 빼고 뒤에거 넣고 그렇게 반복
# beer[1] 오름차순, beer[0]는 내림차순