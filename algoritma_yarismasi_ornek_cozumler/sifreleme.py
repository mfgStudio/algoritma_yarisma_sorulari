#index degeri cift olana 2 ekle, tek olana 1 ekle
print("Algoritma Yarismasina Hosgeldiniz yazisini kriptolama yontemi ile degistirecegiz")
b=[]
c=0
a = "Algoritma Yarismasina Hosgeldiniz"
for item in a:
    if c%2==0:
        x = ord(a[c]) + 2
        #print(x)
        y = chr(x)
        b.append(y)
        #print(y)
        c+=1
    else:
        x = ord(a[c]) -1
        #print(x)
        y = chr(x)
        b.append(y)
        #print(y)
        c+=1
print("".join(b))
