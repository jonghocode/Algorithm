# 성냥이 부족하다면 시간 차이가 적은 곳은 계속 켜두기
# 성냥이 충분하다면 다 하면 됨
# 현재꺼 - (그 전꺼의 +1) 그걸 내림차순으로 정렬하고 k-1개 만큼 총 합에서 빼기
import sys

n, k = map(int, input().split())
lst = [int(sys.stdin.readline().strip()) for i in range(n)]

answer = lst[-1]+1-lst[0]
lst2 = []

for i in range(1, n):
    lst2.append(lst[i] - (lst[i-1]+1))
lst2.sort(reverse=True)

for i in range(k-1):
    answer -= lst2[i]
print(answer)