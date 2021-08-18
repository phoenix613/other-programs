def coder (lang, s, n):
    b = ''
    if lang == 'en':
        for x in s:
            if x.isalpha() == True:
                a = ord(x.lower())
                a = (a + n - 96) % 26 + 96
                if a == 96:
                    a = 122
                if x.lower() != x:
                    b += chr(a).upper()
                else:
                    b += chr(a)
            else:
                b += x
        return b     
    
s = input()
s += ' '
b = ''
j = 0
cnt = 0
for i in range(len(s)):
    if s[i].isalpha() == True:
        cnt += 1
        continue
    else:
        b += coder('en',s[j:i],cnt) + s[i]
        
        cnt = 0
    j = i + 1
        
print(b[:len(b)-1])        