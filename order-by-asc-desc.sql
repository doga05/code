select * from Kitap
insert into Kitap values(23,'Beyaz Geceler', 'Dostoevski',80,5,'2015-09-11','MaviBulut')
insert into Kitap values(24,'Beyaz Geceler', 'Dostoevski',80,5,'2015-09-11','MaviBulut')

--Distinct farkl� olanlar� getirir
select distinct KitapAd from Kitap
select distinct KitapYay�nEvi from Kitap
select distinct KitapYazar from Kitap

insert into Kitap values(21,'K�rk Mantolu Madonna','Sabahattin Ali',160,9,'2016-04-07','Jupiter')
--order by s�ralama
select * from Kitap order by KitapAd desc --descending z'den a'ya
select * from Kitap order by KitapSayfa asc -- b�y�kten k����e
select * from Kitap order by KitapSayfa desc -- artandan azalana b�y�kten k����e

select * from Kitap order by KitapYay�nEvi, KitapFiyat asc