# 이분 탐색(앞에서 부터 하나씩 고르면서 고른 것의 뒤에 것 중에서 0에 가장 가까운 값 찾기)
n = int(input())
lst = list(map(int, input().split()))
answer = 0x7fffffff

for i in range(n-1):
    l, r, k = i+1, n-1, lst[i]*-1
    while l <= r and l > i:
        mid = (l + r) // 2
        if lst[mid] < k:
            l = mid + 1
        elif lst[mid] > k:
            r = mid - 1
        else:
            print(lst[i], lst[mid])
            exit()
        if lst[i] + lst[mid] < 0 and answer > (lst[i]+lst[mid])*-1:
            lans, rans = lst[i], lst[mid]
            answer = (lst[i]+lst[mid])*-1
        elif lst[i] + lst[mid] > 0 and answer > lst[i] + lst[mid]:
            lans, rans = lst[i], lst[mid]
            answer = lst[i] + lst[mid]

print(lans, rans)