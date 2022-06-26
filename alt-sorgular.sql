/*alt sorgu: birden fazla tablonun olmasý durumunda bu tablolarýn herhangi bir alanýnýn herhagi bir deðeriyle ilgili bir kriteri diðer tabloya uygulama*/
select * from Kitap where vergi=(select vergi from Kitap where KitapAd='Palto')--vergisi paltonun vergisine eþit olan kayýtlarý getirir.
select * from Kitap where KitapFiyat=(select KitapFiyat from Kitap where KitapAd='Çalýkuþu')
--birden fazla tablo kullanma:kitapfiyatý ikinci tablodaki sarý renkteki kitaplarýn puanýna eþit olan kitaplarý getir
select * from Kitap where KitapFiyat=(select KitapPuan from Kitap2 where KitapRenk='sarý')--sarý olanýn puaný 7 yani kitap1de fiyatý 7 olanlarý getirir
--3.tablodaki beyaz renkli kitaplarýn kitapbaský sayýsýna göre bu deðeri kitap fiyatla eþleþtirip ona göre sonuçlarý listeleyen sorgu
select * from Kitap where KitapFiyat=(select KitapBaský from Kitap3 where KitapRengi='beyaz')
