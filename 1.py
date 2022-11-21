def ntb(n,b):
    if n==0:
        print(0)
    digits=[]
    while n:
        digits.append(int(n%b))
        n//=b 
    for i in digits:
        print(i,end="")
n=int(input())
b=int(input())
ntb(n,b)



def tpc2(s,c):
    res=0
    for i in range(len(s)):
        if(s[i]==c):
            res=res+1 
    return res 
str1=input();
str2=input();
for i in str2:
    c=i
print(tpc2(str1,c))


