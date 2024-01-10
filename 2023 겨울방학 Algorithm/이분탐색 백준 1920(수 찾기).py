n = int(input())
lst = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
lst.sort()

for k in find:
    l, r, answer = 0, n-1, 0
    while l <= r:
        mid = (l + r) // 2

        if lst[mid] < k:
            l = mid + 1
        elif lst[mid] > k:
            r = mid - 1
        else:
            answer = 1
            break
    print(answer)