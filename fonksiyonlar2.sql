/*tablo sonuçlu fonksiyonlar: skaler fonksiyonlarda return olarak bir tane iþlem yaparýz.
birden fazla deðer dönücekse table kllanýrýz*/
--create function kitappuan(@gelenpuan int)
--returns table
--as
--return select * from Kitap2 where KitapPuan>@gelenpuan

select Kitapadi, KitapRenk from dbo.kitappuan (9)