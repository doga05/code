/*tablo sonu�lu fonksiyonlar: skaler fonksiyonlarda return olarak bir tane i�lem yapar�z.
birden fazla de�er d�n�cekse table kllan�r�z*/
--create function kitappuan(@gelenpuan int)
--returns table
--as
--return select * from Kitap2 where KitapPuan>@gelenpuan

select Kitapadi, KitapRenk from dbo.kitappuan (9)