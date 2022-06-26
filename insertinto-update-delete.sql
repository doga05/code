--INSERT INTO
--select * from Kitap
--insert into Kitap values(20, 'Ýnsan Ne Ýle Yaþar', 'Tolstoy',110,5,'2015-08-12','MaviBulut')
--select * from Kitap
/*insert into Kitap (KitapNo,KitapAd,KitapSayfa,KitapTarih,KitapYayýnEvi)
values (21, 'Suç ve Ceza', 1250,'2016-07-19', 'Merkür')
select * from Kitap*/

--UPDATE tabloadý set alanadý="yenideðer" where þart

update Kitap set KitapYazar='Dostoyevski', KitapFiyat=22 where KitapAd='Suç ve Ceza'
select * from Kitap

update Kitap set KitapFiyat =5 where KitapFiyat<5
select * from Kitap

update Kitap set KitapAd ='Venedik Taciri' where KitapNo = 16

--DELETE from tabloadi
delete from Kitap where KitapNo =8
delete from Kitap where KitapSayfa>880 or KitapFiyat=11