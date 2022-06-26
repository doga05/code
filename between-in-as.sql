select * from Kitap
--as
select KitapFiyat as 'Kitap Ücreti',KitapAd as 'Kitap İsmi' from Kitap --update değil
select KitapAd, KitapYazar, KitapFiyat,KitapFiyat+2 as 'Yeni Fiyat' from Kitap

select * from Kitap where KitapTarih<'2016-01-01'
select * from Kitap where KitapFiyat>9 or KitapYayınEvi='Merkür' order by KitapAd desc
select * from Kitap where KitapYayınEvi in ('Merkür','Ay','Jüpiter')

--between
select * from Kitap where KitapFiyat>=10 and KitapFiyat<20
select * from Kitap where KitapFiyat between 9 and 20