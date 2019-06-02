print("Bizim tarafimizdan verilen denklemi yazmanizi istiyoruz")
a = input("Bir deger giriniz")
toplam = 0
for c in range(1,a):
    toplam += c
#denklemi yanlis yazmisiz gruba, *a degil +a olacak asagida ki dogrudur.
b = 2*int(toplam)+ a
b = b**0.5
print(int(b))
