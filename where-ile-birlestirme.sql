select KitapAd, KitapYazar, KitapTur from Kitap, Kitap2 where Kitap.KitapAd = Kitap2.Kitapadi
select KitapAd, KitapRenk from Kitap k1, Kitap2 k2 where k1.KitapAd=k2.Kitapadi
select KitapAd,KitapTur,KitapRengi from Kitap k1, Kitap2 k2, Kitap3 k3 
where k1.KitapAd=k2.Kitapadi and k2.KitapRenk=k3.KitapRengi