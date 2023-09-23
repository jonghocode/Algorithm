import sys

n, k = map(int, input().split())
k-=5
know = [0]*26
word = []

for i in ('a','n','t','i','c'):
    know[ord(i) - ord('a')] = 1

answer = 0

for i in range(n):
    s = sys.stdin.readline().strip()
    word.append(s[4:len(s)-4]) # 어차피 anta로 시작하고 tica로 끝나기 때문

def back(idx, d):
    global k, answer, n

    if d == k:
        cnt = 0
        for i in range(n):
            sw = 0
            for j in word[i]:
                if know[ord(j) - ord('a')] == 0:
                    sw = 1
                    break
            if sw == 0:
                cnt += 1
        answer = max(answer, cnt)
        return
    # for i in range(n):
    #     for j in word[i]:
    #         if know[ord(j)-ord('a')] == 0:
    #             know[ord(j)-ord('a')] = 1
    #             back(d+1)
    #             know[ord(j)-ord('a')] = 0
    # 오답 : 이렇게 돌릴 필요가 없음
    # 왜냐하면 뭐를 선택하든 26개 중에서 k개만 선택하면 되는거니까
    # 굳이 for문 2개로 체크 할 필요가 없음 매번
    for i in range(idx, 26):
        if know[i] == 0:
            know[i] = 1
            back(i+1, d+1)
            know[i] = 0


back(0, 0)
print(answer)
