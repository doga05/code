--procedure: sogular çok uzun olabilir ve tekrar kullanýlmasý gerekebilir. yani tekrar komut yazma iþinden bizi kurtarýr. kýsmen sýnýf yapýsý gibi
--create procedure Deneme
--as
--select * from KÝtap where KitapSayfa>150--db altýnda programmability altýnda

--execute Deneme --sayfa sayýsý 150den büyük olanlarý getirir

--alter procedure Deneme
--as
--select * from Kitap where KitapSayfa >400
--execute Deneme

--create procedure kitapgetir
--as
--select KitapAd,KitapRenk from Kitap k1 inner join Kitap2 k2 on k1.KitapAd=k2.Kitapadi
--exec kitapgetir

--drop procedure Deneme --siler

--set nocount on
--select * from Kitap -- aralarýndaki tek fark on commands complated yazar

--set nocount off -- off ise 21 rows affected yazar. yani etkilenen satýr sayýsýný gösterir
--select * from Kitap

--create procedure Toplam(@s1 int, @s2 int, @sonuc int output) --dýþardan deðer almak için
--as
--set @sonuc = @s1+@s2
declare @t int
exec Toplam 4,7,@t output
print @t
