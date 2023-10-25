def solution(relation):
    
    def back(n, d, word): # 내가 원하는 깊이, 현재 깊이, 집합을 구하기 위해서 문자열로 더하기
        if d == n: # 원하는 깊이라면
            dict = {}
            for i in range(len(relation)): # 유일하게 구별할 수 있는지 검사(유일성)
                s = ''
                for j in range(len(relation[0])):
                    if tempchk[j] == 1:
                        s += str(relation[i][j])
                if s not in dict: # 딕셔너리로 유일한지 검사
                    dict[s] = 1
                else:
                    return
                
            for k, v in chk.items(): # 부분집합이 있는지 검사(최소성)
                cnt = 0
                for p in k: # 딕셔너리에 있는 문자열
                    for z in word: # 현재 내가 만든 문자열
                        if p == z: # 부분집합인지 확인하기 위해서 같은 개수 체크
                            cnt += 1
                    if cnt == len(k): # 부분집합이라면 return
                        return
            chk[word] = 1 # 아니라면 넣기
            return
        
        for i in range(len(relation[0])): # 백트래킹
            if tempchk[i] == 0:
                tempchk[i] = 1
                back(n, d+1, word+str(i))
                tempchk[i] = 0

    chk = {}
    for i in range(1, len(relation[0])+1):
        tempchk = [0]*(len(relation[0]))
        back(i, 0, "")

    return len(chk)