s=input() #da timeup en code chef

if(len(s)>=10):
    q = int(input())
    if(q>=1 and q<=150000):
        while(q > 0):
            a = input().split()
            a.append('')
            fn = a[0]
            ch = a[1]
            if(fn=='INSERT_LEFT'):
                s = ch+s
            if(fn=='INSERT_RIGHT'):
                s = s+ch
            if(fn=='INSERT_MIDDLE'):
                s = s[:len(s)//2]+ch+s[len(s)//2:]
            if(len(s)>10):
                if(fn=='DELETE_LEFT'):
                    s = s[1:]
                if(fn=='DELETE_RIGHT'):
                    s = s[:len(s)-1]
                if(fn=='DELETE_MIDDLE'):
                    s = s[:len(s)//2]+ s[len(s)//2+1:]
            if(fn=='QUERY'):
                if(len(ch)<=len(s)):
                    c=0
                    ab=s.find(ch)
                    while(ab!=-1):
                        c = c+1
                        ab = s.find(ch,ab+1)
                    print(c)
                else:
                    print(0)
            q = q-1
