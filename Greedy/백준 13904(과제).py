# 하루에 한 문제만 가능 -> 과제를 해야하는 날짜 중 가장 긴 날짜를 기준으로 그 날짜 까지 하루 마다 제일 높은 것만 기록하면 됨

import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
dp = [0 for _ in range(1001)]
MAX = int(1e12)

for d, w in lst:
    sw = MAX
    for i in range(1, d+1): # 1일부터 과제를 제출해야하는 날짜까지 최솟값을 제일 높은 값으로 교체하기
        if dp[i] < sw:
            sw = dp[i]
            idx = i
    
    dp[idx] = w

print(sum(dp))