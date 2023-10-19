import sys

n = int(sys.stdin.readline())

def find(d, s, result):
    if d == len(word):
        print(s)
        return
    
    for i in result:
        if result[i]:
            result[i] -= 1
            find(d+1, s+i, result)
            result[i] += 1

for i in range(n):
    result = {}
    word = sorted(list(sys.stdin.readline().strip()))
    
    for k in word:
        if k not in result:
            result[k] = 1
        else:
            result[k] += 1
    
    find(0, '', result)