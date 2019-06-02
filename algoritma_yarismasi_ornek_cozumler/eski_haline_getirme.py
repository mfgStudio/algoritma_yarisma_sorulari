#sifrelenmis veriyi geri eski haline getirme
print("Algoritma Yarismasina Hosgeldiniz yazisini kriptolama yontemi ile degistirecegiz")
b=['C', 'k', 'i', 'n', 't', 'h', 'v', 'l', 'c', '\x1f', '[', '`', 't', 'h', 'u', 'l', 'c', 'r', 'k', 'm', 'c', '\x1f', 'J', 'n', 'u', 'f', 'g', 'k', 'f', 'h', 'p', 'h', '|']
c=0
d=[]
print("".join(b))

for item in b:
    if c%2==0:
        x = ord(b[c]) - 2
        #print(x)
        #y = chr(x)
        d.append(chr(x))
        #print(y)
        c+=1
    else:
        x = ord(b[c]) + 1
        #print(x)
        y = chr(x)
        d.append(y)
        #print(y)
        c+=1
print("".join(d))
