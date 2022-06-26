--having:kýsýtlama where ile ayný ama group by ile having kullanýlýr
select KitapYayýnEvi, count(KitapAd) as 'toplam' ,
sum(KitapFiyat) as 'Alacak' ,
sum(Vergi) as 'Verecek' ,
(sum(KitapFiyat)-sum(vergi)) as 'Net Bakiye'
from Kitap group by KitapYayýnEvi having count(KitapAd)>=4