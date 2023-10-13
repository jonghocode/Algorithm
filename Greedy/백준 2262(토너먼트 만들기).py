n = int(input())
lst = list(map(int, input().split()))
answer = 0

while len(lst) > 1:
    MAX = -1
    print(lst)
    for i in range(len(lst)):
        if MAX < lst[i]:
            MAX = lst[i]
            idx = i
    
    if idx == 0:
        answer += abs(lst[idx] - lst[idx+1])
    elif idx == len(lst)-1:
        answer += abs(lst[idx] - lst[idx-1])
    else:
        if abs(lst[idx] - lst[idx+1]) < abs(lst[idx] - lst[idx-1]):
            answer += abs(lst[idx] - lst[idx+1])
        else:
            answer += abs(lst[idx] - lst[idx-1])
    lst.pop(idx)

print(answer)