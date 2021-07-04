s = input()
summ = ''
p = ''

for i in range(1,len(s)):
    if s[i-1] == s[i]:
        p+=s[i-1]
        
    elif(s[i-1] != s[i]):
        p+=s[i-1]
        
        summ+=p[0] + str(len(p))
        p = ''
p += s[len(s)-1]
summ+=p[0] + str(len(p))
print(summ)