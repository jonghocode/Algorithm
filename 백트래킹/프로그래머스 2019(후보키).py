def solution(relation):
    
    def back(n, d, word):
        if d == n:
            dict = {}
            for i in range(len(relation)):
                s = ''
                for j in range(len(relation[0])):
                    if tempchk[j] == 1:
                        s += str(relation[i][j])
                if s not in dict:
                    dict[s] = 1
                else:
                    return
            for k, v in chk.items():
                cnt = 0
                for p in k:
                    for z in word:
                        if p == z:
                            cnt += 1
                    if cnt == len(k):
                        return
            chk[word] = 1
            # 0, (2,3), (1, 3, 4)
            return
        
        for i in range(len(relation[0])):
            if tempchk[i] == 0:
                tempchk[i] = 1
                back(n, d+1, word+str(i))
                tempchk[i] = 0

    chk = {}
    for i in range(1, len(relation[0])+1):
        tempchk = [0]*(len(relation[0]))
        back(i, 0, "")

    return len(chk)

print(solution([["100","100","ryan","music","2"], 
["200","200","apeach","math","2"], 
["300","300","tube","computer","3"], 
["400","400","con","computer","4"], 
["500","500","muzi","music","3"], 
["600","600","apeach","music","2"]]))
print(solution([["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]]))

print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))