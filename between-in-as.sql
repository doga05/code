select * from Kitap
--as
select KitapFiyat as 'Kitap �creti',KitapAd as 'Kitap �smi' from Kitap --update de�il
select KitapAd, KitapYazar, KitapFiyat,KitapFiyat+2 as 'Yeni Fiyat' from Kitap

select * from Kitap where KitapTarih<'2016-01-01'
select * from Kitap where KitapFiyat>9 or KitapYay�nEvi='Merk�r' order by KitapAd desc
select * from Kitap where KitapYay�nEvi in ('Merk�r','Ay','J�piter')

--between
select * from Kitap where KitapFiyat>=10 and KitapFiyat<20
select * from Kitap where KitapFiyat between 9 and 20