n = int(input())
dan, ji, tan, vi = map(int, input().split())
lst = []
answer = 0x7fffffff
answerlist = []
chk = []
def back(a, b, c, d, sum, idx):
    global answer

    if a >= dan and b >= ji and c >= tan and d >= vi and answer > sum:
        answer = sum
        answerlist.append([sum, chk[:]])
        return

    for i in range(idx, n):
        chk.append(i+1)
        back(a+lst[i][0], b+lst[i][1], c+lst[i][2], d+lst[i][3], sum+lst[i][4], i+1)
        chk.pop()


for i in range(n):
    lst.append(list(map(int, input().split())))

back(0, 0, 0, 0, 0, 0)

if not answerlist:
    print(-1)
else:
    answerlist.sort(key = lambda x : (x[0], x[1]))
    print(answerlist[0][0])
    print(" ".join(map(str,answerlist[0][1])))
