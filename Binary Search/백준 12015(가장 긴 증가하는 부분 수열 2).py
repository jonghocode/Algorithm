# 자신의 앞에 있는 것 중에서 자신보다 작은 값 중 chk가 가장 큰 값 찾기
# 10 20 10 30 20 50

# 처음 정렬 후 인덱스 배정
# 10 10 20 20 30 50 : temp
# 0   2  1   4   3  5 : 입력받은 인덱스 배정
# 1   1   2      3 : dp / 값 넣기
# 처음엔 값이 작은것을 찾고 다음 부터는 인덱스가 안에 있는 값이 가장 큰 것을 찾으면 됨(현재 인덱스보다 작아야 함)


n = int(input())
lst = list(map(int, input().split()))
temp = sorted([[lst[i], i] for i in range(n)])
dp = [0]*n

for i in range(n):
    now, l, r = lst[i], 0, n
    find = 0
    while l <= r:
        mid = (l + r) // 2
        # print(l, r, i, mid, temp[mid][0], now)
        # print(temp)
        if temp[mid][0] < now:
            if temp[mid][1] < i:
                if find < dp[temp[mid][1]]:
                    find = dp[temp[mid][1]]
            l = mid + 1

        else:
            r = mid - 1

    dp[i] = find+1
    # print(dp)

print(max(dp))