--inner join: a ve b tablosunda ortak olanlar� birle�tirir.
select KitapAd,KitapRenk from Kitap k1 inner join Kitap2 k2 on k1.KitapAd=k2.Kitapadi
--kitapad� ayn� olanlar� renkleriyle getirir
select sum(KitapFiyat) as 'ToplamFiyat', KitapTur from Kitap k1 inner join Kitap2 k2 on k1.KitapAd=k2.Kitapadi group by KitapTur
select KitapAd, KitapTur, KitapRengi from Kitap k1 inner join Kitap2 k2 on k1.KitapAd=k2.Kitapadi inner join Kitap3 k3 on
k2.KitapRenk=k3.KitapRengi
select KitapTur, sum(KitapFiyat) as 'Toplam' from Kitap k1 inner join Kitap2 k2 on
k1.KitapAd=k2.Kitapadi inner join Kitap3 k3 on k2.KitapRenk=k3.KitapRengi group by KitapTur