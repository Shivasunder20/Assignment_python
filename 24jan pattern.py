s=input().lower()
p=input().lower()
if(0<=len(s)<=2000 and 0<=len(p)<=2000):
    if(s==p):
        print('true')
    elif('*' in p or '*' in s):
        print('true')
    elif(len(s)==len(p)):
        a=''
        if '?' in s:
            for i in range(len(s)):
                if(s[i] != '?'):
                    a+=s[i]
                elif(s[i] == '?'):
                    a+=p[i]
        else:
            a=s
        b=''
        if '?' in p:
            for i in range(len(p)):
                if(p[i] != '?'):
                    b+=p[i]
                elif(p[i]=='?'):
                    b+=s[i]
        else:
            b=p
        if(a==b):
            print('true')
        else:
            print('false')
    else:
        print('false')