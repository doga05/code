--INSERT INTO
--select * from Kitap
--insert into Kitap values(20, '�nsan Ne �le Ya�ar', 'Tolstoy',110,5,'2015-08-12','MaviBulut')
--select * from Kitap
/*insert into Kitap (KitapNo,KitapAd,KitapSayfa,KitapTarih,KitapYay�nEvi)
values (21, 'Su� ve Ceza', 1250,'2016-07-19', 'Merk�r')
select * from Kitap*/

--UPDATE tabload� set alanad�="yenide�er" where �art

update Kitap set KitapYazar='Dostoyevski', KitapFiyat=22 where KitapAd='Su� ve Ceza'
select * from Kitap

update Kitap set KitapFiyat =5 where KitapFiyat<5
select * from Kitap

update Kitap set KitapAd ='Venedik Taciri' where KitapNo = 16

--DELETE from tabloadi
delete from Kitap where KitapNo =8
delete from Kitap where KitapSayfa>880 or KitapFiyat=11