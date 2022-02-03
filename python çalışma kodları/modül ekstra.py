'''import modüller#modüller ve modül ekstranın aynı dosyada olması gerekli import diyerek mödüllerdeki fonk.kullanabiliriz

modüller.naber()#hangi fonksiyonu kullanmak istiyorsak ilk önce nerde olduğunu(modüller) daha sonra da fonk.adını yazıyoruz(naber)

print(modüller.mutlak(-120))'''

from modüller import * #modüllerden bütün fonks.çağırır bu pek önerilmez.farklı dosyalarda aynı fonksiyon olursa python hangisini
#kullanacağını bilemez o yüzden kafası karışır o yüzden import kullanmak daha mantıklıdır. fromla sadece bir fonksiyon almak istiyorsak
# from modüller import mutlak yazarız yani hepsi yerine sadece kullanılacak olan fonksiyonun adını yazarız.

naber() #fonksiyonları çağırırken importtan tek farkı sadece fonksiyon isimlerini yazarız.
print(mutlak(-120))