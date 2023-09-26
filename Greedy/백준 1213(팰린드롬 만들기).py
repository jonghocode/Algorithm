s = input()
chk = [0]*26

for i in s:
    chk[ord(i) - ord('A')]+=1

a, b, c = 0, 0, ''
for i in range(len(chk)):
    if chk[i] % 2 == 0: # 짝수 체크
        a+=1
    else: # 홀수 체크
        b+=1
        c = str(chr(i+65)) # 홀수라면 가운데에 넣어야 함

if b>=2: # 안되는 경우 예외처리
    print("I'm Sorry Hansoo")
    exit()

answer = ''
for i in range(len(chk)):
    if chk[i]>= 2:
        for j in range(chk[i]//2): # 반틈 먼저 붙이기
            answer += str(chr(i+65))

if len(s)%2!=0: # 개수가 홀수인것을 중간에 붙이기
    answer+=c
    t = 2
else:
    t = 1

for i in range(len(answer)-t,-1,-1): # 뒷부분 붙이기
    answer+=answer[i]

print(answer)
