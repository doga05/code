select KitapYazar, count(Kitapad) as 'KitapSay�s�' from Kitap group by KitapYazar
select KitapAd, count(KitapAd) as 'Stok' from Kitap group by KitapAd
select KitapYay�nEvi, count(KitapAd) from Kitap group by KitapYay�nEvi order by KitapYay�nEvi asc
--select KitapYay�nEvi, count(KitapAd) from Kitap group by KitapYay�nEvi order by count(KitapAd) asc
select KitapYay�nEvi, sum(KitapFiyat) from Kitap group by KitapYay�nEvi
select KitapYay�nevi, avg(KitapFiyat) from Kitap group by KitapYay�nEvi
select KitapYay�nEvi, max(KitapFiyat) as 'MAX',
min(KitapFiyat) as 'MIN' from Kitap group by KitapYay�nEvi
select KitapYay�nEvi, count(KitapFiyat) from Kitap where KitapFiyat>10 group by KitapYay�nEvi
--select KitapYay�nEvi, count(KitapAd) from Kitap where KitapFiyat>10 group by KitapYay�nEvi yukardakinin ayn�s�

-- K�S�LER TABLOSU
select Meslek, count(Ad) as 'Personel Say�s�' from Kisiler group by Meslek order by count(Ad)
select Sehir, count(Ad) as 'say�' from Kisiler group by Sehir order by Sehir
select Meslek, count(Ad) as 'Personel Say�s�', 
sum(Maas) as 'Toplam Maas',
avg(Maas) as 'Ortalama' 
from Kisiler group by Meslek
select Meslek, max(Maas) as 'MAX' ,min(Maas) as 'MIN' from Kisiler group by Meslek
