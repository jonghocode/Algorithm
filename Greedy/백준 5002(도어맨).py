# 남자와 여자의 차이보다 기억할 수 있는 값 보다 크면 남은 사람들 입장 x

# 차이가 작다면 계속 들여보내주고
# 차이가 꽉 찼으면 뒤에사람

n = int(input())
s = list(input())
man, woman, idx = 0, 0, 0
chk = [0]*len(s)
answer = 0
while idx < len(s):
    if s[idx] == 'W' and chk[idx] == 0: # 여자라면
        if abs(woman+1 - man) <= n: # 바로 입장
            chk[idx] = 1
            woman += 1
            answer += 1
        else: # 바꿔도 안되면 종료
            if idx+1 < len(s) and s[idx+1] != 'W':
                chk[idx+1] = 1
                idx -= 1
                man += 1
                answer += 1
            else:
                break
    elif s[idx] == 'M' and chk[idx] == 0: # 남자라면
        if abs(woman - (man+1)) <= n: # 바로 입장
            chk[idx] = 1
            man += 1
            answer += 1
        else:
            if idx+1 < len(s) and s[idx+1] != 'M':
                chk[idx+1] = 1
                idx -= 1
                woman += 1
                answer += 1
            else: # 바꿔도 안되면 종료
                break

    idx += 1

print(answer)