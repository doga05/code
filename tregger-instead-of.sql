--instead-of: kayıt işlemini gerçekleştirmeden önce gerçekleştiriyor mu gerçekleştirmiyor mu kontrol edersin
--create trigger insdeneme on Kitap2
--instead of insert
--as
--begin
--select 'Ekleme işleminde sorun yok'
--end
--insert into Kitap2 values('Palto','hikaye','vvvv','gri',8)

--create trigger insdeneme2 on Kitap2
--instead of update
--as
--begin
--select 'Kayıt güncellenebilir'
--end
--update Kitap2 set Kitapadi='sefiller' where Kitapadi='Palto'

--create trigger insdeneme3 on Kİtap2
--instead of delete
--as
--begin
--select 'Kayıt Silinebilir'
--end

delete from Kitap2 where Kitapadi='Siyah Lale'