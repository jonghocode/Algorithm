import sys

n = int(input())
answer = 0
line = []
for i in range(n):
    line.append(list(map(int, sys.stdin.readline().strip().split())))

line.sort(key = lambda x : (x[0], x[1]))
st, ed = line[0][0], line[0][1]
# print(line)
for i in range(1, n):
    if ed < line[i][0]:
        answer += ed - st
        st = line[i][0]
        ed = line[i][1]
    else:
        if ed < line[i][1]:
            ed = line[i][1]
    # print(f"i : {i}, st : {st}, ed : {ed}, answer : {answer}")
answer += ed - st
print(answer)