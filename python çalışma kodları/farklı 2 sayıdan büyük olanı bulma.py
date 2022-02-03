a=int(input("Birinci Sayıyı Giriniz: "))
b=int(input("İkinci Sayıyı Giriniz: "))

if (a!=b and a<b):
    print("İkinci sayı daha büyüktür")
elif(a!=b and a>b):
    print("İlk Sayı Daha Büyük")
else:
    print("Satılar eşit")

