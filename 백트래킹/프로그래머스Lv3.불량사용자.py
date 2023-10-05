# 비트마스킹 !!!!!
def solution(user_id, banned_id):
    answer = []
    chk1 = [0 for _ in range(11)]
    dict = {}
    def p(s, l): # banned_id와 맞는지 확인
        if len(s) != len(l):
            return False
        
        for i in range(len(s)):
            if l[i] == '*':
                continue
            elif s[i] != l[i]:
                return False
        return True
        
                
    def back(d):
        if len(banned_id) == d:
            temp = ''
            for i in range(len(user_id)):
                temp+=str(chk1[i])
            if temp not in dict:
                dict[temp] = 1
            return
        for i in range(len(user_id)):
            if chk1[i] == 0 and p(user_id[i], banned_id[d]):
                chk1[i] = 1
                back(d+1)
                chk1[i] = 0
    
    back(0)

    return len(dict)
