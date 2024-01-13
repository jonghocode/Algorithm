# 해시값 : [문자, 숫자]
import sys

def p(s):
    cnt, answer = 1, 0
    for i in s:
        if i <= 'Z':
            temp = ord(i) - 64
        else:
            temp = ord(i) - 70
        answer = (answer+temp*cnt)%X
        cnt = (cnt*59)%X
    return answer

X = 123777
hash = [[] for i in range(X)]
n, m = map(int, input().split())
temp = ['']
for i in range(n):
    s = sys.stdin.readline().strip() 
    hash[p(s)].append((i+1, s))
    temp.append(s)

for i in range(m):
    s = sys.stdin.readline().strip()
    if '0' <= s[0] <= '9':
        print(temp[int(s)])
    else:
        k = p(s)
        for j in hash[k]:
            if j[1] == s:
                print(j[0])
                break
