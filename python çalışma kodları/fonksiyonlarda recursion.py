'''fonksiyonlarda recursion: fonksiyonun kendi kendini çağırması.fonksiyonun içinde aynı fonksiyonu tekrar yağırırız.
1.fonksiyonun bitiş durumunun iyi tanımlanması gerekir. yoksa sonsuza kadar kendini çağırır.
2.fonksiyonun belli şartlarda kendini çağırması gerekiyor.

def topla(liste):
    toplam = 0
    for i in liste:
        toplam +=i
    return toplam
    
print(topla([1,2,3,4])) listedeki sayıları toplayan fonksiyon.recursion hali:'''

def topla(liste):
    if len(liste) == 0:
        return 0
    else:
        return liste [0] + (topla(liste[1:])) #recursion kısmı
    
print(topla([1,2,3,4]))
'''bu fonksiyon şu şekilde çalışır: ilk önce 4 elemanlı bir liste gönderdik. daha sonra listenin boyuna baktı ve 0a eşit olmadığı için
else durumuna girdi.else durumunda return liste[0] yani birinci elemanı aldı ve topla fonksiyonunu aldı daha sonra da 1den sonrasını
yani 2.3.4.elemanları alıp topladı.adım adım göstermek gerekirse;
1.adım return liste[0]+topla(liste[1:])= return 1 + topla ([2,3,4]) daha sonra bu liste kendi içinde tekrar çağırıyor
2.adım return 2 + topla([3,4])
3.adım return 3 + topla([4])
4.adım return 4 + topla([])
5.adım return 0 
son adımdan başlayarak return 0ı aldı daha sonra return 4 ile topladı daha sonra return 3 ile sonra return 2 ve return 1 ile topladı '''

#nihil.ceng.metu.edu.tr