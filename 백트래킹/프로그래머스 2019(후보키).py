def solution(relation):
    global answer
    
    def back(n, d):
        global answer
        if d == n:
            dict = {}
            for i in range(len(relation)):
                s = ''
                for j in range(len(relation[0])):
                    if tempchk[j] == 1:
                        s += relation[i][j]
                if s not in dict:
                    dict[s] = 1
                else:
                    return

            for j in range(len(relation[0])):
                if tempchk[j] == 1 and chk[j] == 0:
                    chk[j] = 1

            answer += 1         
            return
        
        for i in range(len(relation[0])):
            if tempchk[i] == 0:
                tempchk[i] = 1
                back(n, d+1)
                tempchk[i] = 0
    
    answer = 0
    chk = [0]*len(relation)

    for i in range(1, len(relation[0])+1):
        tempchk = [0]*len(relation)
        back(i, 0)
    
    return answer

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