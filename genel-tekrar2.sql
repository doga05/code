/*use Kitaplik

create table Kitap2(
Kitapadi varchar(20),
KitapTur varchar(10),
KitapOzet varchar(50),
KitapRenk varchar(10))*/

--alter table Kitap add Vergi tinyint
/*create table Kitap3(
KitapRengi varchar(10),
KitapBask� varchar(3))*/

/*use Kitaplik
insert into Kitap2 values('Veronika', 'roman', 'fsgsdg', 'k�rm�z�');*/

--select Kitapadi, KitapRenk from Kitap2

--select Kitap2.Kitapadi, Kitap3.KitapRengi from Kitap2, Kitap3 
select * from Kitap where Kitapad='Beyaz Geceler' or Vergi =1
select * from Kitap where Kitapad like 'a%' --ad� a ile ba�layan
select * from Kitap where KitapAd like 'A______________'--A ile ba�layan ve devam�nda olan harf kadar alttan tire
select * from Kitap where KitapYay�nEvi in ('Ay', 'G�ne�')--select * from Kitap where KitapYay�nEvi='ay' or KitapYay�nEvi='G�ne�' ile ayn�

insert into Kitap values(32,'H�lleci', 'Re�at Nuri G�ntekin',75,8,'2016-06-10','J�piter',2)
update Kitap set Vergi=3 where KitapNo=20
delete from Kitap where KitapNo=20

select * from Kitap where KitapAd like '[ab]%'--ad� a ya da b ile ba�layan
select * from Kitap where KitapAd like 'b%e'--b ile ba�layan e ile biten