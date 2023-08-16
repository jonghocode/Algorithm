n = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = 0

for i in range(n):
    sw = 0
    for j in range(n):
        if i == j: continue
        l, r = 0, n-1
        target = lst[i] - lst[j]

        while l <= r:
            mid = (l + r) // 2
            
            if lst[mid] > target:
                r = mid -1
            elif lst[mid] == target and mid != i and mid != j:
                sw = 1
                break
            else :
                l = mid + 1

    if sw == 1:
        answer += 1
        
print(answer)