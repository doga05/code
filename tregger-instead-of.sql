--instead-of: kay�t i�lemini ger�ekle�tirmeden �nce ger�ekle�tiriyor mu ger�ekle�tirmiyor mu kontrol edersin
--create trigger insdeneme on Kitap2
--instead of insert
--as
--begin
--select 'Ekleme i�leminde sorun yok'
--end
--insert into Kitap2 values('Palto','hikaye','vvvv','gri',8)

--create trigger insdeneme2 on Kitap2
--instead of update
--as
--begin
--select 'Kay�t g�ncellenebilir'
--end
--update Kitap2 set Kitapadi='sefiller' where Kitapadi='Palto'

--create trigger insdeneme3 on K�tap2
--instead of delete
--as
--begin
--select 'Kay�t Silinebilir'
--end

delete from Kitap2 where Kitapadi='Siyah Lale'