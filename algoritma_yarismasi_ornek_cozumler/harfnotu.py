print("Harf notu Hesaplama")
while True:
    vize = input("Vizeniz ? = ")
    final = input("Finaliniz ? = ")
    if(vize<100 or final<100):
        break

but = 0
ortalama = (vize*0.4+final*0.6)
print(ortalama)
if(final<50):
    if(ortalama<50):
        print("Butunlemeye girmeniz gerekiyor")
        print("FF ALDINIZ")
        print("Suan girdinizzzz")
        while True:
            but = input("But sonucunuz ? = ")
            ortalama = (vize*0.4+but*0.6)
            if(but<100):
                print("ortalamaniz", ortalama)
                break
            
    else:
        print("FD ALDINIZ")
elif(final>50):
    if(ortalama<50):
        print("FD ALDINIZ")
        while True:
            but = input("But sonucunuz ? = ")
            ortalama = (vize*0.4+but*0.6)
            print("ortalamaniz", ortalama)
            if(but<100):
                print("ortalamaniz", ortalama)
                break
            
    elif(ortalama>50):
        print("ortamlaniz = ",ortalama)
        if(ortalama>85):
            print("AA")
        elif(ortalama<85 or ortalama>75):
            print("BA")
        elif(ortalama<75 or ortalama>65):
            print("BB")
        elif(ortalama<65 or ortalama>55):
            print("CB")
        else:
            print("CC")
    