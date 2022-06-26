/*alt sorgu: birden fazla tablonun olmas� durumunda bu tablolar�n herhangi bir alan�n�n herhagi bir de�eriyle ilgili bir kriteri di�er tabloya uygulama*/
select * from Kitap where vergi=(select vergi from Kitap where KitapAd='Palto')--vergisi paltonun vergisine e�it olan kay�tlar� getirir.
select * from Kitap where KitapFiyat=(select KitapFiyat from Kitap where KitapAd='�al�ku�u')
--birden fazla tablo kullanma:kitapfiyat� ikinci tablodaki sar� renkteki kitaplar�n puan�na e�it olan kitaplar� getir
select * from Kitap where KitapFiyat=(select KitapPuan from Kitap2 where KitapRenk='sar�')--sar� olan�n puan� 7 yani kitap1de fiyat� 7 olanlar� getirir
--3.tablodaki beyaz renkli kitaplar�n kitapbask� say�s�na g�re bu de�eri kitap fiyatla e�le�tirip ona g�re sonu�lar� listeleyen sorgu
select * from Kitap where KitapFiyat=(select KitapBask� from Kitap3 where KitapRengi='beyaz')
