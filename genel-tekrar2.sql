/*use Kitaplik

create table Kitap2(
Kitapadi varchar(20),
KitapTur varchar(10),
KitapOzet varchar(50),
KitapRenk varchar(10))*/

--alter table Kitap add Vergi tinyint
/*create table Kitap3(
KitapRengi varchar(10),
KitapBaskı varchar(3))*/

/*use Kitaplik
insert into Kitap2 values('Veronika', 'roman', 'fsgsdg', 'kırmızı');*/

--select Kitapadi, KitapRenk from Kitap2

--select Kitap2.Kitapadi, Kitap3.KitapRengi from Kitap2, Kitap3 
select * from Kitap where Kitapad='Beyaz Geceler' or Vergi =1
select * from Kitap where Kitapad like 'a%' --adı a ile başlayan
select * from Kitap where KitapAd like 'A______________'--A ile başlayan ve devamında olan harf kadar alttan tire
select * from Kitap where KitapYayınEvi in ('Ay', 'Güneş')--select * from Kitap where KitapYayınEvi='ay' or KitapYayınEvi='Güneş' ile aynı

insert into Kitap values(32,'Hülleci', 'Reşat Nuri Güntekin',75,8,'2016-06-10','Jüpiter',2)
update Kitap set Vergi=3 where KitapNo=20
delete from Kitap where KitapNo=20

select * from Kitap where KitapAd like '[ab]%'--adı a ya da b ile başlayan
select * from Kitap where KitapAd like 'b%e'--b ile başlayan e ile biten