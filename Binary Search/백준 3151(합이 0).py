n = int(input())
lst = list(map(int, input().split()))
lst.sort()

answer = 0
for i in range(n):
    for j in range(i+1, n):
        k = -(lst[i] + lst[j])
        l, r = i+1, n-1
        while l <= r:
            mid = (l + r) // 2
            
            if lst[mid] > k:
                r = mid - 1
            elif lst[mid] < k:
                l = mid + 1
            else:
                answer += 1
                break

print(answer)