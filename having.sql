--having:k�s�tlama where ile ayn� ama group by ile having kullan�l�r
select KitapYay�nEvi, count(KitapAd) as 'toplam' ,
sum(KitapFiyat) as 'Alacak' ,
sum(Vergi) as 'Verecek' ,
(sum(KitapFiyat)-sum(vergi)) as 'Net Bakiye'
from Kitap group by KitapYay�nEvi having count(KitapAd)>=4