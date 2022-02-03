import time
#Sırala sınıfı oluşturuldu
class Sırala:
    # Yapıcı fonksiyona liste olacak a parametresini ekledik. Daha sonra üye değişkenleri atandı.
    def init(self,a):
        self._store_unsorted=a
        geri_donus=self._comp_alg(a)
        self._store_sorted=geri_donus[0]
        self._mintime_alg=geri_donus[1]
    # _comp_alg fonksiyonu oluşturuldu. Süre hesaplar.
    def _comp_alg(self,a):
        baslangic=time.time()
        siralanmis=self.kabarcikli_siralama(a.copy())
        bitis=time.time()
        kabarcikli_zaman=bitis-baslangic

        baslangic=time.time()
        self.eklemeli_siralama(a.copy())
        bitis=time.time()
        eklemeli_zaman=bitis-baslangic
        if eklemeli_zaman<kabarcikli_zaman:
            return (siralanmis,"Araya Eklemeli Sıralama",eklemeli_zaman)
        else:
            return (siralanmis,"Kabarcıklı Sıralama",kabarcikli_zaman)

    def kabarcikli_siralama(self,a): # Kabarcıklı sıralama fonksiyonu oluşturuldu.
        for i in range(len(a)):
            for j in range(len(a)-1-i):
                if a[j]>a[j+1]: # Art arda gelen elemanların değeri karşılaştırır. ilki ikinciden büyükse 
                    a[j],a[j+1]=a[j+1],a[j] # Yerlerini değiştiriyor.
        return 1

    def eklemeli_siralama(self,a): # Eklemeli sıralama fonksiyonu oluşturuldu.
        for i in range(1,len(a)):
            cur=a[i]
            j=i
            while j>0 and a[j-1]>cur: # j 0'dan büyük ve a[j-1] cur'dan büyük olduğu sürece
                a[j]=a[j-1] # a[j] bir öncekine eşitlenir 
                j-=1 # j 1 azaltılır
            a[j]=cur # Dizi başlangıca gelmiştir ya da eklemek istediğimiz değerden daha küçük bir değer vardır.
        return a