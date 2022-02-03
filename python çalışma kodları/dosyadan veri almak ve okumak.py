dosya = open("dosyadeneme.txt","r")#bu dosya varsa okur eğer yoksa hata verir.hatadan kurtulmak için try except kullanılabilr.

#print(dosya.read())

'''read() bütün yazılanları okur
readline() dosyanın en başındaki satırı alır alt alta yazılırsa kaç satır varsa o kadar satırı okur satırlar bitmişse boşluk basar
readlines() bütün satırları alır ve satırları liste şeklinde verir.
olmak üzere 3 fonksiyon vardır'''

#liste = dosya.readlines()
#print(liste[1])

#büyük dosyalar için dosya.close() fonksiyonu kullanılır.

'''dosyaları beeli bir yere kadar okuma ya da belli bir yerden sonra okuma:
dosyalarda yazılan her kelimenin bir harfi ya da her karakteri 1 bayt eder. örneğin: bir dosyada doğa yazıyor bu 4 harfin her biri
1 bayttır ve toplam 4 bayt eder.'''

#dosya = open("dosyada okuma.txt","w")
with open("dosyada okuma.txt","r") as dosya:
    dosya.seek(10)#bu fonksiyon belli bir yerden sonra okumasına yarar.parantezin içine nerden sonra okumasını istediğimizi yazarız
    print(dosya.read(5))#readin içine parametre atarsak o kadar karakter verir
    #dosya.seek(5)# bu da en başından 5 tzne ilerler 10un üstüne eklemez
    #print(dosya.read())
    '''dosya.seek(10)
       str1 = dosya.read(5)
       dosya.seek(15)
       str2 = dosya.read(5)
       
       print(str1,str2)
    '''


