valid=['0','1','2','5','6','8','9']
a=int(input())
lists=[]
b=1
y=1
while(y<=a):
  str1=str(b)
  c=0
  for i in str1:
    if(i in valid):
      c+=1
    if(c==len(str1)):
      lists.append(str1)
      y+=1
    b+=1
  final=l[len(lists)-1]
  f=int(final)
  print(final)
