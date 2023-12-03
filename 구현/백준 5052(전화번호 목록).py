import sys

def p(n):
    lst = [sys.stdin.readline().strip() for _ in range(n)]
    lst.sort()
    for j in range(n-1):
        if lst[j][:] == lst[j+1][0:len(lst[j])]:
            return("YES")
    return("NO")
t = int(input())
for i in range(t):
    n = int(input())
    print(p(n))