f=open("vowel,consonants.txt","w")
b=("mani\n","jyothi\n","manju\n")
f.writelines(b)
f=open("vowel,consonants.txt","a")
f.write("SREEKHGFS")
print(f)
f=open("vowel,consonants.txt","r")
print(f.read())
f.close
f=open("vowel,consonants.txt","r")
a=f.read()
print(a)
i=0
upper=0
lower=0
vowel=0
consonant=0
while i<len(a):
    if a[i].isupper():
        upper+=1
    if a[i].islower():
        lower+=1
    if a[i] in ("a","e","i","o","u","A","E","I","O","U"):
        vowel+=1
    else:
        consonant+=1
    i=i+1
print("upper",upper)
print("lower",lower)
print("vowel",vowel)
print("consonant",consonant)
