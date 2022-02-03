'''yerel değişkenler: girdilerin içinde olan değişkenlerdir.
global değişkenler: fonksiyonlar ya da iflerden önce tanımlanan değişkenlerdir.dışardaki atamaların değerlerini değiştirebiliriz.'''

a= 10 #global değişken 

def fonk():
    global a # fonksiyon dışında bir a var ve biz bunu değiştirmek istiyoruz önceden 2 ve 10 basıyordu ama şimdi böyle 2 ve 2 bastırıcak
    a = 2 #yerel değişken
    print(a)
fonk()
print(a)