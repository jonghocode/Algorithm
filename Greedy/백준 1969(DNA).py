# 정답을 구해야하는 s는 각 문자열의 1~n까지의 행에 있는 인덱스마다
# 가장 많이 나온 문자가 답이고, 합은 전체 n개의 행 중 가장 많이 나온 값의 차다.
n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]
answer, cnt = '', 0

for i in range(m):
    dict = {}
    for j in range(n):
        if lst[j][i] not in dict:
            dict[lst[j][i]] = 1
        else:
            dict[lst[j][i]] += 1
    
    # temp = []
    # for k, v in dict.items():
    #     temp.append([k, v])
    # temp.sort(key = lambda x : (-x[1], x[0]))
    temp = sorted([[k, v] for k, v in dict.items()], key = lambda x : (-x[1], x[0]))
    answer += temp[0][0]
    cnt += n - temp[0][1]

print(answer)
print(cnt)