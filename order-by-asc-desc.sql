select * from Kitap
insert into Kitap values(23,'Beyaz Geceler', 'Dostoevski',80,5,'2015-09-11','MaviBulut')
insert into Kitap values(24,'Beyaz Geceler', 'Dostoevski',80,5,'2015-09-11','MaviBulut')

--Distinct farklý olanlarý getirir
select distinct KitapAd from Kitap
select distinct KitapYayýnEvi from Kitap
select distinct KitapYazar from Kitap

insert into Kitap values(21,'Kürk Mantolu Madonna','Sabahattin Ali',160,9,'2016-04-07','Jupiter')
--order by sýralama
select * from Kitap order by KitapAd desc --descending z'den a'ya
select * from Kitap order by KitapSayfa asc -- büyükten küçüðe
select * from Kitap order by KitapSayfa desc -- artandan azalana büyükten küçüðe

select * from Kitap order by KitapYayýnEvi, KitapFiyat asc