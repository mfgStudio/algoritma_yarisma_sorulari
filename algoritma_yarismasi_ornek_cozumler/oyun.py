import random
print("random fonksiyonunu kullanarak oyun yazacagiz")
print("Oyunda amacimiz programin random bir deger uretmesi ve bizim bilmeye calismamiz")
print("\nOyunumuz Basliyor")
def gout():
    print("Gorusuruzz")
    exit()

def goto() :
    asd=random.randint(1,10)
    i=1
    print(asd)
    #random deger atamasi yaptik
    f=1
    print("\n1 ile 10 arasinda rastgele sayi belirlendi\n3 hakkiniz var bulmak icin!!")
    for i in range(1,4):
        print(str(f)+".ci hakkiniz")
        f+=1
        giris = input("\nNedir sizce? =>")
        if(giris != asd):
            print("Bilemediniz "+str(3-i) + " hakkiniz kaldi")
            if(f == 4):
                re = input(">>Tekrar oynamak icin 1'ye tiklayin\n>> Bitirmek icin 1 disinda herhangi bir sayi tusuna basmaniz yeterli!\n ==>")
                if(re!=1):
                    re=2
                if(re ==1):
                    goto()
                else:
                    gout()
                
        else:
            re = input("Dogru bildiniz tebrix\n>>Tekrar oynamak icin 1'ye tiklayin\n>> Bitirmek icin 1 disinda herhangi bir sayi tusuna basmaniz yeterli")
            if(re!=1):
                re=2
            if(re ==1):
                goto()
            else:
                gout()
goto()


