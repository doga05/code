--outpu i�lemi: bir tabloda etkilenen kay�tlar� listelemek i�in kullan�lan yap�
--declare @yeni table(
--renk varchar(10),
--baski tinyint,
--derece varchar(1)
--)
--insert into Kitap3 output inserted.KitapRengi,inserted.KitapBask�,inserted.KitapDerece into @yeni values('mavi',21,'a')

--select * from @yeni -- buras� sadece yani ekledi�imiz de�erleri g�sterir yani etkilenenleri ama select * from kitap3 yaz�l�rsa bu de�erler g�z�kmez 
--��nk� yapay bir ekleme ve kitap3 tablosunda da g�z�kmez

declare @silinen table(
renk varchar(10),
baski tinyint,
derece varchar(1))
delete from Kitap3 output deleted.KitapRengi,deleted.KitapBask�,deleted.KitapDerece into @silinen where KitapDerece ='d'
select * from @silinen
