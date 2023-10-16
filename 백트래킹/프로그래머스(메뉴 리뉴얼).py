def solution(orders, course):
    answer = []
    
    def back(slen, menu, idx, now, chk):
        
        if len(menu) == slen:
            T = []
            
            for i in range(len(orders)):
                MAX = -1
                d = 1
                
                if chk[i] == 0: # 기준이 되는 orders를 제외
                    cnt = 0
                    for j in menu:
                        if j in orders[i]:
                            cnt += 1
                    if cnt == slen:
                        d += 1
                    if d >= 2:
                        T.append([d, menu])

            if T:
                T.sort(key = lambda x : -x[0])
                lst.append(T[0][1])
                p = T[0][0]
                for k in range(1, len(T)):
                    if p!=T[k][0]:
                        break
                    lst.append(T[k][1])
            return
        
        for i in range(idx, len(now)):
            back(slen, menu+now[i], i+1, now, chk)
        
                
    
    for i in course:
        dict = {}
        for j in range(len(orders)):
            lst = []
            chk = [0]*len(orders)
            chk[j] = 1
            back(i, '', 0, orders[j], chk)
            for k in lst:
                st = []
                for j in k:
                    st.append(j)
                st.sort()
                te = ''.join(st)
                if te not in dict:
                    dict[te] = 1
                else:
                    dict[te] += 1
        temp = []
        for k, v in dict.items():
            temp.append([k,v])
        if temp:
            temp.sort(key = lambda x : -x[1])
            p = temp[0][1]
            answer.append(temp[0][0])
            for k in range(1, len(temp)):
                if p!=temp[k][1]:
                    break
                answer.append(temp[k][0])
    
    answer.sort()
    return answer