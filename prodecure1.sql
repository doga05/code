--procedure: sogular �ok uzun olabilir ve tekrar kullan�lmas� gerekebilir. yani tekrar komut yazma i�inden bizi kurtar�r. k�smen s�n�f yap�s� gibi
--create procedure Deneme
--as
--select * from K�tap where KitapSayfa>150--db alt�nda programmability alt�nda

--execute Deneme --sayfa say�s� 150den b�y�k olanlar� getirir

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
--select * from Kitap -- aralar�ndaki tek fark on commands complated yazar

--set nocount off -- off ise 21 rows affected yazar. yani etkilenen sat�r say�s�n� g�sterir
--select * from Kitap

--create procedure Toplam(@s1 int, @s2 int, @sonuc int output) --d��ardan de�er almak i�in
--as
--set @sonuc = @s1+@s2
declare @t int
exec Toplam 4,7,@t output
print @t
