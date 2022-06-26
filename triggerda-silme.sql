--create trigger SilmeKontrol on Kitap2
--after delete
--as 
--begin
--select 'Kayýt Tablodan Silindi'
--end
--delete from Kitap2 where KitapOzet='eeeeee'


--create trigger SilmeKontrol2 on Kitap2
--after delete
--as
--begin
--update Guncelleme set Sayac=Sayac-1
--end 
delete from Kitap2 where KitapOzet='aaaaa'