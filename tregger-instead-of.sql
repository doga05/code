--instead-of: kayýt iþlemini gerçekleþtirmeden önce gerçekleþtiriyor mu gerçekleþtirmiyor mu kontrol edersin
--create trigger insdeneme on Kitap2
--instead of insert
--as
--begin
--select 'Ekleme iþleminde sorun yok'
--end
--insert into Kitap2 values('Palto','hikaye','vvvv','gri',8)

--create trigger insdeneme2 on Kitap2
--instead of update
--as
--begin
--select 'Kayýt güncellenebilir'
--end
--update Kitap2 set Kitapadi='sefiller' where Kitapadi='Palto'

--create trigger insdeneme3 on KÝtap2
--instead of delete
--as
--begin
--select 'Kayýt Silinebilir'
--end

delete from Kitap2 where Kitapadi='Siyah Lale'