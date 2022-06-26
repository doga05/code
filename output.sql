--outpu iþlemi: bir tabloda etkilenen kayýtlarý listelemek için kullanýlan yapý
--declare @yeni table(
--renk varchar(10),
--baski tinyint,
--derece varchar(1)
--)
--insert into Kitap3 output inserted.KitapRengi,inserted.KitapBaský,inserted.KitapDerece into @yeni values('mavi',21,'a')

--select * from @yeni -- burasý sadece yani eklediðimiz deðerleri gösterir yani etkilenenleri ama select * from kitap3 yazýlýrsa bu deðerler gözükmez 
--çünkü yapay bir ekleme ve kitap3 tablosunda da gözükmez

declare @silinen table(
renk varchar(10),
baski tinyint,
derece varchar(1))
delete from Kitap3 output deleted.KitapRengi,deleted.KitapBaský,deleted.KitapDerece into @silinen where KitapDerece ='d'
select * from @silinen
