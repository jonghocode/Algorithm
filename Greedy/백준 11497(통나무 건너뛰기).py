import sys

t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, sys.stdin.readline().strip().split()))
    lst.sort()

    for j in range(n-1, 1, -2): # 배열을 다시 만들기
        lst.append(lst.pop(j-2))
    
    answer = -1
    for j in range(n-1):
        answer = max(answer, abs(lst[j]-lst[j+1]))
    print(answer)
