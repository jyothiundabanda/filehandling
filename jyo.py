i=1
while i<=5:
    user=input("enter the number:")
    f=open("abc.txt",'a')
    f.write(user+"\n")
    i+=1
c=open("abc.txt",'r')
d=c.readlines()
f1=open("bb.txt","w")
f2=open("cc.txt","w")
print(d)
j=0
while j<len(d):
    if 'a' in d[j]:
        f1.write(d[j])
    else:
        f2.write(d[j])
    j+=1