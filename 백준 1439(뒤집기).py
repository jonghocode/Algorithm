s = input()

chk = [0, 0]
st = s[0]
chk[int(st)] = 1
for i in range(1,len(s)):
    if st == s[i]:
        continue
    else:
        o = int(s[i])
        st = s[i]
        chk[o] +=1

print(min(chk))
    