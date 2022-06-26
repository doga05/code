select KitapYazar, count(Kitapad) as 'KitapSayýsý' from Kitap group by KitapYazar
select KitapAd, count(KitapAd) as 'Stok' from Kitap group by KitapAd
select KitapYayýnEvi, count(KitapAd) from Kitap group by KitapYayýnEvi order by KitapYayýnEvi asc
--select KitapYayýnEvi, count(KitapAd) from Kitap group by KitapYayýnEvi order by count(KitapAd) asc
select KitapYayýnEvi, sum(KitapFiyat) from Kitap group by KitapYayýnEvi
select KitapYayýnevi, avg(KitapFiyat) from Kitap group by KitapYayýnEvi
select KitapYayýnEvi, max(KitapFiyat) as 'MAX',
min(KitapFiyat) as 'MIN' from Kitap group by KitapYayýnEvi
select KitapYayýnEvi, count(KitapFiyat) from Kitap where KitapFiyat>10 group by KitapYayýnEvi
--select KitapYayýnEvi, count(KitapAd) from Kitap where KitapFiyat>10 group by KitapYayýnEvi yukardakinin aynýsý

-- KÝSÝLER TABLOSU
select Meslek, count(Ad) as 'Personel Sayýsý' from Kisiler group by Meslek order by count(Ad)
select Sehir, count(Ad) as 'sayý' from Kisiler group by Sehir order by Sehir
select Meslek, count(Ad) as 'Personel Sayýsý', 
sum(Maas) as 'Toplam Maas',
avg(Maas) as 'Ortalama' 
from Kisiler group by Meslek
select Meslek, max(Maas) as 'MAX' ,min(Maas) as 'MIN' from Kisiler group by Meslek
